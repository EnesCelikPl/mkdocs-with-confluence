from mkdocs_with_confluence.plugin import MkdocsWithConfluence

def test_plugin_loads_config():
    plugin = MkdocsWithConfluence()

    config = {
        "host_url": "https://fake.atlassian.net/wiki",
        "space": "TEST",
        "parent_page_name": "Home",
        "username": "fake@example.com",
        "api_token": "fake-token"
    }

    result = plugin.load_config(config)
    assert result == ([], [])

def test_basic_plugin_behavior():
    plugin = MkdocsWithConfluence()
    assert plugin is not None
