from happiness.filters import find_country, filter_by_region, filter_by_score_range, to_float, filter_by_life_expectancy

def test_find_country(data, country_name="Czechia"):
    """Test vyhledávání země podle názvu."""
    # Vyhledání dat pro Českou republiku
    result = find_country(data, country_name)
    # Ověření, že výsledek je seznam
    assert isinstance(result, list)
    # Ověření, že seznam není prázdný
    assert len(result) > 0
    # Ověření, že první záznam odpovídá České republice
    assert result[0]["Country"] == country_name


def test_filter_by_region(data, region_name="Western Europe"):
    """Test filtrování podle regionu."""
    # Filtrování dat pro region "Western Europe"
    result = filter_by_region(data, region_name)
    # Ověření, že výsledek je seznam
    assert isinstance(result, list)
    # Ověření, že seznam není prázdný
    assert len(result) > 0
    # Ověření, že všechny záznamy patří do správného regionu
    for r in result:
        assert r["Regional indicator"] == region_name


def test_filter_by_score_range(data, min_score=7.0, max_score=8.0, score_key="Happiness score"):
    """Test filtrování podle rozsahu skóre."""
    # Filtrování dat podle skóre v rozsahu 7.0 až 8.0
    result = filter_by_score_range(data, min_score, max_score, score_key)
    # Ověření, že výsledek je seznam
    assert isinstance(result, list)
    # Ověření, že seznam není prázdný
    assert len(result) > 0
    # Ověření, že všechny záznamy mají skóre v zadaném rozsahu
    for r in result:
        score = to_float(r[score_key])
        assert min_score <= score <= max_score
        

def test_filter_by_life_expectancy(data, min_expectancy=70.0, max_expectancy=80.0, expectancy_key="Life expectancy"):
    """Test filtrování podle očekávané délky života."""
    # Filtrování dat podle očekávané délky života v rozsahu 70.0 až 80.0
    result = filter_by_life_expectancy(data, min_expectancy, max_expectancy, expectancy_key)
    # Ověření, že výsledek je seznam
    assert isinstance(result, list)
    # Ověření, že seznam není prázdný
    assert len(result) > 0
    # Ověření, že všechny záznamy mají očekávanou délku života v zadaném rozsahu
    for r in result:
        expectancy = to_float(r[expectancy_key])
        assert min_expectancy <= expectancy <= max_expectancy