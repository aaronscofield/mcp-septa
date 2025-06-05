"""station.py"""

from enum import Enum


class RegionalRailStation(Enum):
    """Enum representing all SEPTA Regional Rail station parameters.

    Each enum member uses the station's parameter value (API-friendly format)
    and includes the full station name as a comment for reference.
    """

    # 9th Street - C
    NINTH_ST = "9th St"  # 9th Street Station
    THIRTIETH_STREET_STATION = "30th Street Station"  # 30th Street Station
    FORTY_NINTH_ST = "49th St"  # 49th Street
    AIRPORT_TERMINAL_A = "Airport Terminal A"  # Airport Terminal A
    AIRPORT_TERMINAL_B = "Airport Terminal B"  # Airport Terminal B
    AIRPORT_TERMINAL_C_D = "Airport Terminal C-D"  # Airport Terminals C & D
    AIRPORT_TERMINAL_E_F = "Airport Terminal E-F"  # Airport Terminals E & F
    ALLEGHENY = "Allegheny"  # Allegheny
    ALLEN_LANE = "Allen Lane"  # Allen Lane
    AMBLER = "Ambler"  # Ambler
    ANGORA = "Angora"  # Angora
    ARDMORE = "Ardmore"  # Ardmore
    ARDSLEY = "Ardsley"  # Ardsley
    BALA = "Bala"  # Bala
    BERWYN = "Berwyn"  # Berwyn
    BETHAYRES = "Bethayres"  # Bethayres
    BRIDESBURG = "Bridesburg"  # Bridesburg
    BRISTOL = "Bristol"  # Bristol
    BRYN_MAWR = "Bryn Mawr"  # Bryn Mawr
    CARPENTER = "Carpenter"  # Carpenter
    CHALFONT = "Chalfont"  # Chalfont
    CHELTEN_AVENUE = "Chelten Avenue"  # Chelten Avenue
    CHELTENHAM = "Cheltenham"  # Cheltenham
    CHESTER_TC = "Chester TC"  # Chester Transportation Center
    CHESTNUT_HILL_EAST = "Chestnut Hill East"  # Chestnut Hill East
    CHESTNUT_HILL_WEST = "Chestnut Hill West"  # Chestnut Hill West
    CHURCHMANS_CROSSING = "Churchmans Crossing"  # Churchmans Crossing
    CLAYMONT = "Claymont"  # Claymont
    CLIFTON_ALDAN = "Clifton-Aldan"  # Clifton-Aldan
    COLMAR = "Colmar"  # Colmar
    CONSHOHOCKEN = "Conshohocken"  # Conshohocken
    CORNWELLS_HEIGHTS = "Cornwells Heights"  # Cornwells Heights
    CRESTMONT = "Crestmont"  # Crestmont
    CROYDON = "Croydon"  # Croydon
    CRUM_LYNNE = "Crum Lynne"  # Crum Lynne
    CURTIS_PARK = "Curtis Park"  # Curtis Park
    CYNWYD = "Cynwyd"  # Cynwyd

    # D - G
    DARBY = "Darby"  # Darby
    DAYLESFORD = "Daylesford"  # Daylesford
    DELAWARE_VALLEY_COLLEGE = "Delaware Valley College"  # Delaware Valley College
    DEVON = "Devon"  # Devon
    DOWNINGTOWN = "Downingtown"  # Downingtown
    DOYLESTOWN = "Doylestown"  # Doylestown
    EAST_FALLS = "East Falls"  # East Falls
    EASTWICK_STATION = "Eastwick Station"  # Eastwick Station
    EDDINGTON = "Eddington"  # Eddington
    EDDYSTONE = "Eddystone"  # Eddystone
    ELKINS_PARK = "Elkins Park"  # Elkins Park
    ELM_ST = "Elm St"  # Elm Street, Norristown
    ELWYN_STATION = "Elwyn Station"  # Elwyn
    EXTON = "Exton"  # Exton
    FERN_ROCK_TC = "Fern Rock TC"  # Fern Rock Transportation Center
    FERNWOOD = "Fernwood"  # Fernwood–Yeadon
    FOLCROFT = "Folcroft"  # Folcroft
    FOREST_HILLS = "Forest Hills"  # Forest Hills
    FT_WASHINGTON = "Ft Washington"  # Fort Washington
    FORTUNA = "Fortuna"  # Fortuna
    FOX_CHASE = "Fox Chase"  # Fox Chase
    GERMANTOWN = "Germantown"  # Germantown
    GLADSTONE = "Gladstone"  # Gladstone
    GLENOLDEN = "Glenolden"  # Glenolden
    GLENSIDE = "Glenside"  # Glenside
    GRAVERS = "Gravers"  # Gravers
    GWYNEDD_VALLEY = "Gwynedd Valley"  # Gwynedd Valley

    # H - K
    HATBORO = "Hatboro"  # Hatboro
    HAVERFORD = "Haverford"  # Haverford
    HIGHLAND = "Highland"  # Highland
    HIGHLAND_AVE = "Highland Ave"  # Highland Avenue
    HOLMESBURG_JCT = "Holmesburg Jct"  # Holmesburg Junction
    IVY_RIDGE = "Ivy Ridge"  # Ivy Ridge
    MARKET_EAST = "Market East"  # Jefferson Station (Market East)
    JENKINTOWN_WYNCOTE = "Jenkintown-Wyncote"  # Jenkintown-Wyncote

    # L - O
    LANGHORNE = "Langhorne"  # Langhorne
    LANSDALE = "Lansdale"  # Lansdale
    LANSDOWNE = "Lansdowne"  # Lansdowne
    LAWNDALE = "Lawndale"  # Lawndale
    LEVITTOWN = "Levittown"  # Levittown
    LINK_BELT = "Link Belt"  # Link Belt
    MAIN_ST = "Main St"  # Main Street, Norristown
    MALVERN = "Malvern"  # Malvern
    MANAYUNK = "Manayunk"  # Manayunk
    MARCUS_HOOK = "Marcus Hook"  # Marcus Hook
    MEADOWBROOK = "Meadowbrook"  # Meadowbrook
    MEDIA = "Media"  # Media
    MELROSE_PARK = "Melrose Park"  # Melrose Park
    MERION = "Merion"  # Merion
    MIQUON = "Miquon"  # Miquon
    MORTON = "Morton"  # Morton
    MT_AIRY = "Mt Airy"  # Mount Airy
    MOYLAN_ROSE_VALLEY = "Moylan-Rose Valley"  # Moylan-Rose Valley
    NARBERTH = "Narberth"  # Narberth
    NESHAMINY_FALLS = "Neshaminy Falls"  # Neshaminy Falls
    NEW_BRITAIN = "New Britain"  # New Britain
    NEWARK = "Newark"  # Newark
    NOBLE = "Noble"  # Noble
    NORRISTOWN_TC = "Norristown TC"  # Norristown Transportation Center
    NORTH_BROAD_ST = "North Broad St"  # North Broad
    NORTH_HILLS = "North Hills"  # North Hills
    NORTH_PHILADELPHIA = "North Philadelphia"  # North Philadelphia
    NORTH_WALES = "North Wales"  # North Wales
    NORWOOD = "Norwood"  # Norwood
    OLNEY = "Olney"  # Olney
    ORELAND = "Oreland"  # Oreland
    OVERBROOK = "Overbrook"  # Overbrook

    # P - S
    PAOLI = "Paoli"  # Paoli
    PENLLYN = "Penllyn"  # Penllyn
    PENNBROOK = "Pennbrook"  # Pennbrook
    PENN_MEDICINE_STATION = (
        "Penn Medicine Station"  # Penn Medicine Station (University City)
    )
    PHILMONT = "Philmont"  # Philmont
    PRIMOS = "Primos"  # Primos
    PROSPECT_PARK = "Prospect Park"  # Prospect Park
    QUEEN_LANE = "Queen Lane"  # Queen Lane
    RADNOR = "Radnor"  # Radnor
    RIDLEY_PARK = "Ridley Park"  # Ridley Park
    ROSEMONT = "Rosemont"  # Rosemont
    ROSLYN = "Roslyn"  # Roslyn
    RYDAL = "Rydal"  # Rydal
    RYERS = "Ryers"  # Ryers
    SECANE = "Secane"  # Secane
    SEDGWICK = "Sedgwick"  # Sedgwick
    SHARON_HILL = "Sharon Hill"  # Sharon Hill
    SOMERTON = "Somerton"  # Somerton
    SPRING_MILL = "Spring Mill"  # Spring Mill
    ST_DAVIDS = "St. Davids"  # St. Davids
    ST_MARTINS = "St. Martins"  # St. Martins
    STENTON = "Stenton"  # Stenton
    STRAFFORD = "Strafford"  # Strafford
    SUBURBAN_STATION = "Suburban Station"  # Suburban Station
    SWARTHMORE = "Swarthmore"  # Swarthmore

    # T - W
    TACONY = "Tacony"  # Tacony
    TEMPLE_U = "Temple U"  # Temple University
    THORNDALE = "Thorndale"  # Thorndale
    TORRESDALE = "Torresdale"  # Torresdale
    TRENTON = "Trenton"  # Trenton Transit Center
    TREVOSE = "Trevose"  # Trevose
    TULPEHOCKEN = "Tulpehocken"  # Tulpehocken
    UPSAL = "Upsal"  # Upsal
    VILLANOVA = "Villanova"  # Villanova
    WALLINGFORD = "Wallingford"  # Wallingford
    WARMINSTER = "Warminster"  # Warminster
    WASHINGTON_LANE = "Washington Lane"  # Washington Lane
    WAYNE = "Wayne"  # Wayne
    WAYNE_JCT = "Wayne Jct"  # Wayne Junction
    WEST_TRENTON = "West Trenton"  # West Trenton
    WHITFORD = "Whitford"  # Whitford
    WILLOW_GROVE = "Willow Grove"  # Willow Grove
    WILMINGTON = "Wilmington"  # Wilmington
    WISSAHICKON = "Wissahickon"  # Wissahickon
    WISTER = "Wister"  # Wister
    WOODBOURNE = "Woodbourne"  # Woodbourne
    WYNDMOOR = "Wyndmoor"  # Wyndmoor
    WYNNEFIELD_AVENUE = "Wynnefield Avenue"  # Wynnefield Avenue
    WYNNEWOOD = "Wynnewood"  # Wynnewood

    # X - Z
    YARDLEY = "Yardley"  # Yardley
