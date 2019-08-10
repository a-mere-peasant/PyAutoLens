class HyperImageSky(object):
    def __init__(self, sky_scale=0.0):
        """Class for scaling the background sky map and background noise_map-map of an regular.

        Parameters
        -----------
        sky_scale : float
            The value by which the background scale is increased or decreased (electrons per second).
        noise_scale : float
            The factor by which the background noise_maps is increased.
        """
        self.sky_scale = sky_scale

    def image_scaled_sky_from_image(self, image):
        """Compute a new regular with the background sky level normal. This can simply multiple by a constant factor \
        (assuming a uniform background sky) because the regular is in units electrons per second.

        Parameters
        -----------
        image : ndarray
            The regular before scaling (electrons per second).
        """
        return image + self.sky_scale


class HyperBackgroundNoise(object):
    def __init__(self, noise_scale=0.0):
        """Class for scaling the background sky map and background noise_map-map of an regular.

        Parameters
        -----------
        sky_scale : float
            The value by which the background scale is increased or decreased (electrons per second).
        noise_scale : float
            The factor by which the background noise_maps is increased.
        """
        self.noise_scale = noise_scale

    def noise_map_scaled_noise_from_noise_map(self, noise_map):
        """Compute a normal noise_maps regular from the background noise_maps regular.

        Parameters
        -----------
        noise_map : ndarray
            The noise_maps before scaling (electrons per second).
        background_noise : ndarray
            The background noise_maps values (electrons per second).
        """
        return noise_map + self.noise_scale
