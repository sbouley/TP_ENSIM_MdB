function [] = plot_CBF(b_grid, grid, path)

%    Parameters
%    ----------
%    b_grid : array (51 x 31)
%        Value of the beamforming map on each calculation nodes (shape : 51 x 31)
%    grid : array (51 x 31)
%        Coordinates of the calculation grid (shape : 51 x 31)
%    path : string
%        path to DATA repository
%
%    Returns
%    -------
%    None.

 
  p_ref = 2e-5;
  dyn = 8;
  carto_dB = 20*log10((abs(b_grid))./p_ref);
  guitar_picture = 'photo_guitar.jpg';

  Z1 = imread(strcat(path, '/', guitar_picture));
  figure
  image(linspace(min(grid(:,1)),max(grid(:,1)),10), linspace(min(grid(:,2)),max(grid(:,2)),10),Z1);
  hold on
  p=pcolor(linspace(min(grid(:,1)),max(grid(:,1)),size(carto_dB,1)), linspace(min(grid(:,2)),max(grid(:,2)),size(carto_dB,2)),flipud(transpose(carto_dB)));
  set(p,'facealpha',0.3)
  colorbar;
  vmax = floor(max(carto_dB(:)));
  vmin = vmax-dyn;

  caxis([vmin vmax])
  shading interp;
  title('CBF')
  xlabel('x (cm)')
  ylabel('y (cm)')
  
end


function [] = plot_PSF(psf_grid, grid)
    
%     Parameters
%     ----------
%     psf_grid : array (51 x 31)
%         Value of the point spread function in reference of one calculation nods (shape : 51 x 31)
%     grid : array (51 x 31)
%         Coordinates of the calculation grid (shape : 51 x 31)
% 
%     Returns
%     -------
%     None.


%    PSF 
  dyn_PSF = 30;

  carto_PSF = 20*log10((abs(psf_grid)));
  figure
  
  pcolor(linspace(min(grid(:,1)),max(grid(:,1)),size(carto_PSF,1)), linspace(min(grid(:,2)),max(grid(:,2)),size(carto_PSF,2)),transpose(carto_PSF));
  colorbar;
  vmax = floor(max(carto_PSF(:)));
  vmin = vmax-dyn_PSF;
  caxis([vmin vmax])
  shading interp;
  
  
  title('PSF')
  xlabel('node index')
  ylabel('node index')
  
end