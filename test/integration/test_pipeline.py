from src.analysis import non_linear, galaxy_prior
from src.profiles import light_profiles, mass_profiles


def test_pipeline():
    # Create an optimizer
    optimizer_1 = non_linear.MultiNest()

    # Define galaxy priors
    source_galaxy_prior = galaxy_prior.GalaxyPrior(light_profile=light_profiles.EllipticalSersic,
                                                   variable_redshift=True)
    lens_galaxy_prior = galaxy_prior.GalaxyPrior(spherical_mass_profile=mass_profiles.EllipticalIsothermal,
                                                 shear_mass_profile=mass_profiles.ExternalShear, variable_redshift=True)

    # Add the galaxy priors to the optimizer
    optimizer_1.variable.source_galaxies = [source_galaxy_prior]
    optimizer_1.variable.lens_galaxies = [lens_galaxy_prior]

    optimizer_1.create_param_names()
