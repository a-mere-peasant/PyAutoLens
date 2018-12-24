from matplotlib import pyplot as plt

from autolens.data.array.plotters import plotter_util
from autolens.lens.plotters import lens_plotter_util


def plot_fit_subplot(fit, should_plot_mask=True, positions=None,
                     units='arcsec', figsize=None, aspect='equal',
                     cmap='jet', norm='linear', norm_min=None, norm_max=None, linthresh=0.05,
                     linscale=0.01,
                     cb_ticksize=10, cb_fraction=0.047, cb_pad=0.01,
                     titlesize=10, xlabelsize=10, ylabelsize=10, xyticksize=10,
                     mask_pointsize=10, position_pointsize=10.0, grid_pointsize=1,
                     output_path=None, output_filename='sensitivity_fit', output_format='show'):
    """Plot the model datas of an analysis, using the *Fitter* class object.

    The visualization and output type can be fully customized.

    Parameters
    -----------
    fit : autolens.sensitivity_fitting.SensitivityProfileFit
        Class containing fitting between the model datas and observed lens datas (including residual_map, chi_squared_map etc.)
    """

    rows, columns, figsize_tool = plotter_util.get_subplot_rows_columns_figsize(number_subplots=9)

    mask = lens_plotter_util.get_mask(fit=fit.fit_normal, should_plot_mask=should_plot_mask)

    if figsize is None:
        figsize = figsize_tool

    plt.figure(figsize=figsize)
    plt.subplot(rows, columns, 1)

    kpc_per_arcsec = fit.tracer_normal.image_plane.kpc_per_arcsec_proper

    lens_plotter_util.plot_image(fit=fit.fit_normal, mask=mask, positions=positions, image_plane_pix_grid=None,
                                 as_subplot=True,
                                 units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
                                 cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh,
                                 linscale=linscale,
                                 cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
                                 titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize,
                                 xyticksize=xyticksize,
                                 grid_pointsize=grid_pointsize, position_pointsize=position_pointsize,
                                 mask_pointsize=mask_pointsize,
                                 output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 4)

    lens_plotter_util.plot_model_data(fit=fit.fit_normal, mask=mask, as_subplot=True,
                                      units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
                                      cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh,
                                      linscale=linscale,
                                      cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
                                      titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
                                      output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 5)

    lens_plotter_util.plot_residual_map(fit=fit.fit_normal, mask=mask, as_subplot=True,
                                        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
                                        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh,
                                        linscale=linscale,
                                        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
                                        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
                                        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 6)

    lens_plotter_util.plot_chi_squared_map(fit=fit.fit_normal, mask=mask, as_subplot=True,
                                           units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
                                           cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh,
                                           linscale=linscale,
                                           cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
                                           titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
                                           output_path=output_path, output_filename='', output_format=output_format)
    
    plt.subplot(rows, columns, 7)

    lens_plotter_util.plot_model_data(fit=fit.fit_sensitive, mask=mask, as_subplot=True,
                                      units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
                                      cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh,
                                      linscale=linscale,
                                      cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
                                      titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
                                      output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 8)

    lens_plotter_util.plot_residual_map(fit=fit.fit_sensitive, mask=mask, as_subplot=True,
                                        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
                                        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh,
                                        linscale=linscale,
                                        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
                                        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
                                        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 9)

    lens_plotter_util.plot_chi_squared_map(fit=fit.fit_sensitive, mask=mask, as_subplot=True,
                                           units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
                                           cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh,
                                           linscale=linscale,
                                           cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
                                           titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
                                           output_path=output_path, output_filename='', output_format=output_format)

    plotter_util.output_subplot_array(output_path=output_path, output_filename=output_filename,
                                      output_format=output_format)

    plt.close()