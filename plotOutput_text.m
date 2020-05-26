function plotOutput_text( filename )

% This function visualizes your output of the algorithm, given a text file.

% Read the node path
nodePath = load(filename,'-ascii');
% Check the dimension of the input
if size(nodePath,2) ~= 9
    disp('The dimension of input is incorrect. Please check the input and try again.');
    return;
end
nodePath = reshape(nodePath',[3 3 size(nodePath,1)]);

% Setup the figure/window for the game
figure('Name','Puzzle Solver');
plot(-1. -1)
axis([0 3 0 3])
set(gca,'xTick',0:3)
set(gca,'yTick',0:3)
set(gca,'xTickLabel','')
set(gca,'yTickLabel','')
shg
rectangle('Position',[0 0 3 3],'FaceColor',[153 76 0]/255,'EdgeColor','black','LineWidth',3);
currentNode = nodePath(:,:,1);
for i=1:3
    for j=1:3
        if currentNode(i,j)~=0
            rectangle('Position',[j-0.925 3.075-i 0.85 0.85],'FaceColor',[255 255 204]/255,'Curvature',0.2);
            text(j-0.5,3.5-i,num2str(currentNode(i,j)),'FontSize',24)
        end
    end
end

% Start the puzzle solver
pause on
for n=2:size(nodePath,3)
    nextNode = nodePath(:,:,n);
    currentBlank = find(currentNode==0);
    nextBlank = find(nextNode==0);
    [row(1),col(1)] = quorem(sym(currentBlank),sym(3));
    if col(1)==0
        col(1) = 3;
    else
        row(1) = row(1)+1;
    end
    [row(2),col(2)] = quorem(sym(nextBlank),sym(3));
    if col(2)==0
        col(2) = 3;
    else
        row(2) = row(2)+1;
    end
    traverse = double([linspace(row(2)-0.925,row(1)-0.925);linspace(3.075-col(2),3.075-col(1));...
                linspace(row(2)-0.5,row(1)-0.5);linspace(3.5-col(2),3.5-col(1))]);
    for t=1:100
        cla
        rectangle('Position',[0 0 3 3],'FaceColor',[153 76 0]/255,'EdgeColor','black','LineWidth',3);
        for i=1:3
            for j=1:3
                if (currentNode(i,j)~=0)&&(nextNode(i,j)~=0)
                    rectangle('Position',[j-0.925 3.075-i 0.85 0.85],'FaceColor',[255 255 204]/255,'Curvature',0.2);
                    text(j-0.5,3.5-i,num2str(currentNode(i,j)),'FontSize',24)
                end
            end
        end
        rectangle('Position',[traverse(1,t) traverse(2,t) 0.85 0.85],'FaceColor',[255 255 204]/255,'Curvature',0.2);
        text(traverse(3,t),traverse(4,t),num2str(currentNode(nextBlank)),'FontSize',24)
        pause(0.01);
    end
    currentNode = nodePath(:,:,n);
end

end