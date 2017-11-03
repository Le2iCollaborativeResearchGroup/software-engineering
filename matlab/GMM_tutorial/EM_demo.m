% Test EM algorithm
im = rgb2gray(imread('cameraman.jpg'));
[mask,mu,v,p]=EMSeg(im,2);

% for k = 1:nColors
%     color = im;
%     color(mask ~= k) = 0;
%     segmented_images{k} = color;
% end
% 
% imshow(segmented_images{1}), title('objects in cluster 1');

figure(2), imshow(mask, [])