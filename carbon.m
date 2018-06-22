% Data is roughly based on Nepal's last 50 years of Co2 emissions
% x label refers to the number of years
% y label refers to carbon-dioxide emission

clear all; close all; clc
x = load('data/1co2.dat'); y = load('data/2co2.dat');

m = length(y); % number of training examples


% Plot the training data
figure;

plot(x, y, 'o');
title('Nepal Co2 emissions prediction')
ylabel('Emission-(metric tons per capita)')
xlabel('Years')

% Gradient descent
x = [ones(m, 1) x]; % Add a column of ones to x
theta = zeros(size(x(1,:)))'; % initialize fitting parameters
MAX_ITR = 1500;
alpha = 0.07;

for num_iterations = 1:MAX_ITR
    % This is a vectorized version of the 
    % gradient descent update formula
    
    grad = (1/m).* x' * ((x * theta) - y);
    
    % Here is the actual update
    theta = theta - alpha .* grad;
   
end
% print theta to screen
theta

exact_theta = (x' * x)\x' * y

% Plot the linear fit
hold on; % keep previous plot visible
plot(x(:,2), x*exact_theta, '-')
legend('Emission', 'Predictor','Location','northwest')
hold off




% Predict values for age 2030 and 2050
predict1 = [1, 2030] *exact_theta
predict2 = [1, 2050] *exact_theta


% Calculate J matrix

% Grid over which we will calculate J
theta0_vals = linspace(-3, 3, 100);
theta1_vals = linspace(-1, 1, 100);

% initialize J_vals to a matrix of 0's
J_vals = zeros(length(theta0_vals), length(theta1_vals));

for i = 1:length(theta0_vals)
	  for j = 1:length(theta1_vals)
	  t = [theta0_vals(i); theta1_vals(j)];    
	  J_vals(i,j) = (0.5/m) .* (x * t - y)' * (x * t - y);
    end
end

% We need to transpose J_vals before calling surf, or else the axes will be flipped
J_vals = J_vals';
% Surface plot
figure;
surf(theta0_vals, theta1_vals, J_vals)
xlabel('\theta_0'); ylabel('\theta_1');
