#!/bin/zsh

echo "Hello! CS Mac Users."
echo "This is zsh setting files installer for macOS 14 or later."

cd ~
if [ -f ".zprofile" ]; then
	mv .zprofile .zprofile.bak
	cp /Volumes/MacTeX_install2025/ChangeZsh_env/Files/zprofile .zprofile
else
	cp /Volumes/MacTeX_install2025/ChangeZsh_env/Files/zprofile .zprofile
fi

if [ -f ".zshrc" ]; then
	mv .zshrc .zshrc.bak
	cp /Volumes/MacTeX_install2025/ChangeZsh_env/Files/zshrc .zshrc
else
	cp /Volumes/MacTeX_install2025/ChangeZsh_env/Files/zshrc .zshrc
fi

chmod 644 .zprofile
chmod 644 .zshrc

source ~/.zshrc

