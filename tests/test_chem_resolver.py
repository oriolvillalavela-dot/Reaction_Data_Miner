"""
Test module for chemical resolution functionality.
"""
def test_chemical_entity_imports():
    """Verify that imports work properly."""
    try:
        from surf_extractor.agents.chem_resolver_agent import ChemResolverAgent
        assert True
    except ImportError:
        assert False, "Failed to import ChemResolverAgent"
