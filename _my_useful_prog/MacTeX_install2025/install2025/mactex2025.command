#!/bin/zsh

echo "Hello, Everyone!"
echo "This script will setup MacTeX2025 related files for MacOS 15."

export PATH=/usr/local/texlive/2025/bin/universal-darwin/:$PATH # for M1/M2/M3 chips
# export PATH=/usr/local/texlive/2025/bin/x86_64-darwin/:$PATH # for Intel chips

# https://contrib.texlive.info/current/packages.txt # Package list
sudo tlmgr update --self --all
sudo tlmgr repository add https://mirror.ctan.org/systems/texlive/tlcontrib tlcontrib
sudo tlmgr pinning add tlcontrib "*"
sudo tlmgr install japanese-otf-nonfree ptex-fontmaps-macos cjk-gs-integrate-macos

sudo tlmgr path add

sudo cjk-gs-integrate --link-texmf --cleanup
sudo cjk-gs-integrate-macos --link-texmf --fontdef-add=cjkgs-macos-highsierra.dat

## bundled Hiragino OpenType fonts (OS X 10.13 High Sierra & later)
pushd /usr/local/texlive/texmf-local/fonts/truetype/cjk-gs-integrate/
sudo ln -s "/System/Library/Fonts/ヒラギノ明朝 ProN.ttc"     HiraginoSerif.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"  HiraginoSansR-W4.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W0.ttc" HiraginoSans-W0.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W1.ttc" HiraginoSans-W1.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc" HiraginoSans-W2.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc" HiraginoSans-W3.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc" HiraginoSans-W4.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc" HiraginoSans-W5.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc" HiraginoSans-W6.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc" HiraginoSans-W7.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc" HiraginoSans-W8.ttc
sudo ln -s "/System/Library/Fonts/ヒラギノ角ゴシック W9.ttc" HiraginoSans-W9.ttc

## TFM files of Base 14 fonts
sudo mkdir -p /usr/local/texlive/texmf-local/fonts/tfm/local/adobe/ly1/
pushd /usr/local/texlive/texmf-local/fonts/tfm/local/adobe/ly1/
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/pcrb8y.tfm cob.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/pcrbo8y.tfm cobo.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/pcrr8y.tfm com.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/pcrro8y.tfm coo.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/phvr8y.tfm hv.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/phvb8y.tfm hvb.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/phvbo8y.tfm hvbo.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/phvro8y.tfm hvo.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/psyr.tfm sy.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/ptmb8y.tfm tib.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/ptmbi8y.tfm tibi.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/ptmbo8y.tfm tibo.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/ptmri8y.tfm tii.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/ptmro8y.tfm tio.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/ly1/ptmr8y.tfm tir.tfm
sudo ln -s /usr/local/texlive/2025/texmf-dist/fonts/tfm/adobe/zapfding/pzdr.tfm zd.tfm

sudo mkdir -p /usr/local/texlive/texmf-local/tex/platex/pxchfon/
sudo mkdir -p /usr/local/texlive/texmf-local/tex/platex/plistings/
pushd /usr/local/texlive/texmf-local/tex/platex/pxchfon/
sudo cp /Volumes/MacTeX_install2025/tex/platex/pxchfon/pxchfon-extras.def .
pushd /usr/local/texlive/texmf-local/tex/platex/plistings/
sudo cp /Volumes/MacTeX_install2025/tex/platex/plistings.sty .

sudo mktexlsr

sudo kanji-config-updmap-sys --jis2004 hiragino-highsierra-pron
sudo updmap-sys --setoption jaEmbed hiragino-highsierra-pron

sudo updmap-sys
