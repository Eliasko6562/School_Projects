from happiness.data_loader import load_data
from happiness.filters import find_country, filter_by_region, filter_by_score_range, to_float, filter_by_life_expectancy

def main():
    try:
        csv_path = "data/world_happiness_2023.csv"
        data = load_data(csv_path, delimiter=";")

        print(f"Načteno {len(data)} záznamů.")
        print(f"První záznam: {data[0]}")

        print("\n🔹 Vyhledání země 'Czechia':")
        country = find_country(data, "Czechia")
        print(country)

        print("\n🔹 Filtrování podle regionu 'Western Europe':")
        region = filter_by_region(data, "Western Europe")
        print(f"Nalezeno {len(region)} zemí v regionu Western Europe.")

        print("\n🔹 Filtrování podle skóre (7.0 - 8.0):")
        filtered = filter_by_score_range(data, 7.0, 8.0)
        print(f"Nalezeno {len(filtered)} zemí s hodnotou štěstí v rozmezí 7.0-8.0.")
        
        print("\n🔹 Filtrování podle očekávané délky života (70.0 - 80.0):")
        life_expectancy = filter_by_life_expectancy(data, 70.0, 80.0, "Life expectancy")
        print(f"Nalezeno {len(life_expectancy)} zemí s očekávanou délkou života v rozmezí 70.0-80.0.")
    except FileNotFoundError:
        print("Chyba: Soubor nebyl nalezen.")

 
if __name__ == "__main__":
    main()
