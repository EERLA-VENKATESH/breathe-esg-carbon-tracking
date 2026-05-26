\# SOURCES.md - Data Source Research



\## SAP Data (Procurement \& Fuel)



\*\*Format Studied\*\*: Flat file CSV exports from SAP MM (Materials Management) module



\*\*Key Real-World Quirks\*\*:

\- German column headers: 'Menge' (Quantity), 'ME' (Unit), 'Datum' (Date)

\- Date format: DD.MM.YYYY instead of ISO YYYY-MM-DD

\- Material numbers: 18-digit zero-padded codes

\- Plant codes: 4-digit numeric codes (e.g., '1100' = Berlin plant)

\- Units: L (Liters), M3 (Cubic meters), KG (Kilograms), TO (Metric Tons)



\*\*Sample Data Created\*\*:

\- Fuel procurement records (diesel, natural gas, heating oil, gasoline, propane)

\- Plant location mapping file



\*\*Production Concerns\*\*:

\- Encoding issues (UTF-8 vs Latin-1)

\- Decimal separator: comma vs period (1.234,56 vs 1234.56)



\## Utility Data (Electricity)



\*\*Format Studied\*\*: CSV exports from utility business portals (E.ON, Vattenfall style)



\*\*Key Real-World Quirks\*\*:

\- Non-calendar billing periods: e.g., 15th January to 14th February

\- Meter multipliers: CT/PT ratios (40x, 80x for large industrial meters)

\- Estimated readings flagged when meter communication fails

\- 15-minute interval data for smart meters

\- Peak/Off-peak tariff structures



\*\*Sample Data Created\*\*:

\- Interval meter readings (15-minute granularity)

\- Monthly billing summaries with peak/off-peak breakdown

\- Meter registry with facility mapping



\*\*Production Concerns\*\*:

\- Timezone handling (UTC vs local)

\- Missing intervals due to meter communication failures



\## Travel Data (Corporate Travel)



\*\*Format Studied\*\*: SAP Concur expense report exports (CSV)



\*\*Key Real-World Quirks\*\*:

\- Missing distances: Only airport codes provided (e.g., TXL → LHR)

\- Cabin class affects emissions (Economy = 1x, Business = 1.5x, First = 2x)

\- Radiative forcing multiplier (2x) for flights at altitude

\- Hotel emissions based on nights, not cost

\- Car rental distances often missing (estimated from fuel charges)



\*\*Sample Data Created\*\*:

\- Flight records with origin/destination airports, cabin class

\- Hotel stays with number of nights

\- Car rentals with vehicle type



\*\*Production Concerns\*\*:

\- Airport code validation (3-letter IATA codes)

\- Distance calculation methodology (Great-circle vs ICAO)

\- Multi-city trips (stopover handling)



\## Emission Factors Reference



\*\*Sources Researched\*\*:

\- DEFRA (UK government) - 2024 conversion factors

\- EPA (US Environmental Protection Agency) - eGRID

\- IPCC (Intergovernmental Panel on Climate Change) - GWP values

\- ICAO (International Civil Aviation Organization) - flight emissions

\- Google Travel Impact Model - modern flight methodology

