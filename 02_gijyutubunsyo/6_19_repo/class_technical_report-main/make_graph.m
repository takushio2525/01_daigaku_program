load("bi_result.csv")
load("new_result.csv")

figure;
set(0,'defaultAxesFontSize',25);
set(0,'defaultAxesFontName','Times New Roman');
set(0,'defaultTextFontSize',25);
set(0,'defaultTextFontName','Times New Roman');


subplot(2,1,1);

plot(bi_result(:,1),bi_result(:,3),'-b','Linewidth',2);
hold on;
plot(new_result(:,1),new_result(:,3),'-r','Linewidth',2);

xlabel("繰り返し回数: {\it n}");

ylabel("推定解: {\it x_n}");

legend('２分法','ニュートン法')

grid on;

subplot(2,1,2);

semilogy(bi_result(:,1),bi_result(:,2),'-b','Linewidth',2);
hold on;
semilogy(new_result(:,1),new_result(:,2),'-r','Linewidth',2);

xlabel("繰り返し回数: {\it n}");
ylabel("誤差: {\it |x_{n-1}-x_{n}|}")

legend('２分法','ニュートン法')


grid on;