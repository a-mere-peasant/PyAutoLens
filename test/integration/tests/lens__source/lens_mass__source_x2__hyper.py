import autofit as af
from autolens.model.galaxy import galaxy_model as gm
from autolens.model.galaxy import galaxy as g
from autolens.model.profiles import light_profiles as lp, mass_profiles as mp
from autolens.pipeline.phase import phase_imaging
from autolens.pipeline import pipeline as pl
from test.integration.tests import runner

test_type = "lens__source"
test_name = "lens_mass__source_x2__hyper"
data_type = "lens_mass__source_smooth"
data_resolution = "LSST"


def make_pipeline(name, phase_folders, optimizer_class=af.MultiNest):

    phase1 = al.PhaseImaging(
        phase_name="phase_1",
        phase_folders=phase_folders,
        galaxies=dict(
            lens=al.GalaxyModel(redshift=0.5, mass=al.mass_profiles.EllipticalIsothermal),
            source_0=al.GalaxyModel(redshift=1.0, sersic=al.EllipticalSersic),
        ),
        optimizer_class=optimizer_class,
    )

    phase1.optimizer.const_efficiency_mode = True
    phase1.optimizer.n_live_points = 60
    phase1.optimizer.sampling_efficiency = 0.7

    class AddSourceGalaxyPhase(al.PhaseImaging):
        def pass_priors(self, results):

            self.galaxies.lens = results.from_phase("phase_1").variable.galaxies.lens
            self.galaxies.source_0 = results.from_phase(
                "phase_1"
            ).variable.galaxies.source_0

    phase2 = AddSourceGalaxyPhase(
        phase_name="phase_2",
        phase_folders=phase_folders,
        galaxies=dict(
            lens=al.GalaxyModel(redshift=0.5, mass=al.mass_profiles.EllipticalIsothermal),
            source_0=al.GalaxyModel(redshift=1.0, sersic=al.EllipticalSersic),
            source_1=al.GalaxyModel(redshift=1.0, sersic=al.EllipticalSersic),
        ),
        optimizer_class=optimizer_class,
    )

    phase2.optimizer.const_efficiency_mode = True
    phase2.optimizer.n_live_points = 60
    phase2.optimizer.sampling_efficiency = 0.7

    phase2 = phase2.extend_with_multiple_hyper_phases(hyper_galaxy=True)

    class HyperLensSourcePlanePhase(al.PhaseImaging):
        def pass_priors(self, results):

            self.galaxies.lens = results.from_phase("phase_2").variable.galaxies.lens

            self.galaxies = results.from_phase("phase_2").variable.galaxies

            self.galaxies.source_0.hyper_galaxy = (
                results.last.hyper_combined.constant.galaxies.source_0.hyper_galaxy
            )

            self.galaxies.source_1.hyper_galaxy = (
                results.last.hyper_combined.constant.galaxies.source_1.hyper_galaxy
            )

    phase3 = HyperLensSourcePlanePhase(
        phase_name="phase_3",
        phase_folders=phase_folders,
        galaxies=dict(
            lens=al.GalaxyModel(
                redshift=0.5, mass=al.mass_profiles.EllipticalIsothermal, hyper_galaxy=al.HyperGalaxy
            ),
            source_0=al.GalaxyModel(
                redshift=1.0, light=al.light_profiles.EllipticalSersic, hyper_galaxy=al.HyperGalaxy
            ),
            source_1=al.GalaxyModel(
                redshift=1.0, light=al.light_profiles.EllipticalSersic, hyper_galaxy=al.HyperGalaxy
            ),
        ),
        optimizer_class=optimizer_class,
    )

    phase3.optimizer.const_efficiency_mode = True
    phase3.optimizer.n_live_points = 40
    phase3.optimizer.sampling_efficiency = 0.8

    return al.PipelineImaging(name, phase1, phase2, phase3)


if __name__ == "__main__":
    import sys

    runner.run(sys.modules[__name__])
