from auto_lens.analysis import fitting
from auto_lens.imaging import grids
from auto_lens.analysis import ray_tracing
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.level = logging.DEBUG


class Analysis(object):
    def __init__(self, image, mask, grid_size_sub=4):
        """
        An analysis object. Once set up with an image and mask it takes a set of objects describing a model and
        determines how well they fit the image.

        Parameters
        ----------
        image: Image
            An image of a lens with associated metadata
        mask: Mask
            A mask describing the region of the image to be modelled
        grid_size_sub: int
            The size of the sub-pixel grid for which values should be calculated
        """
        self.image = image
        self.mask = mask
        self.image_grid_collection = grids.GridCoordsCollection.from_mask(mask, grid_size_sub=grid_size_sub,
                                                                          blurring_shape=image.psf.shape)

    def run(self, lens_galaxies, source_galaxies, instrumentation):
        """
        Runs the analysis. Determines how well the supplied model fits the image.

        Parameters
        ----------
        lens_galaxies: [Galaxy]
            A collection of galaxies that form the lens
        source_galaxies: [Galaxy]
            A collection of galaxies that are being lensed
        instrumentation: Instrumentation
            A class describing instrumental effects

        Returns
        -------
        result: Result
            An object comprising the final model instances generated and a corresponding likelihood
        """

        tracer = ray_tracing.Tracer(lens_galaxies, source_galaxies, self.image_grid_collection)
        likelihood = fitting.likelihood_for_image_tracer_and_instrumentation(self.image, tracer, instrumentation)
        return Analysis.Result(likelihood, lens_galaxies, source_galaxies, instrumentation)

    class Result(object):
        def __init__(self, likelihood, lens_galaxies, source_galaxies, instrumentation):
            self.likelihood = likelihood
            self.lens_galaxies = lens_galaxies
            self.source_galaxies = source_galaxies
            self.instrumentation = instrumentation