# TODO: We would get patterns from our DB
# TODO: Try parsing from a table

# ElPaso full string
#     """
# Page: 1 Purchase Order EL PASO PHOENIX PUMPS INC. 26 BUTTERFIELD TRAIL BLVD EL PASO, TX  79906 9157571300 P.O. Number: Order Date: 6/27/2024 Vendor Number: 0931525 Ship To: FILTER ELEMENT STORE PO BOX 68004 INDIANAPOLIS, IN  46268 EL PASO PHOENIX PUMPS, INC. 26 BUTTERFIELD TRAIL BLVD. EL PASO, TX  79906 0070717 Vendor: ** Order must SHIP COMPLETE unless otherwise noted by EPPPI personnel. ** Confirm To: Phone:(800) 551-0774 (800) 651-5806 Fax: Terms Ship VIA UPSG 7/16/2024 NET 30 Item Code Unit Ordered Unit Cost Amount Date Req'd @ Dest. User Logon:   PUMPS300 sales@filterelementstore.com Vendor Number E87848 1801063 EACH 30 39.50 1,185.00 000 DEKKER VACUUM 1801063 VACUUM EXHAUST FILTER  (EQUIVALENT) 1809001 EACH 30 8.69 260.70 000 DEKKER VACUUM 1809001 VACUUM FILTER REPLACEMENT PLEASE CONFIRM ORDER* FX: (915) 757-1322 OR  EMAIL: rosieb@elpasophoenixpumps.com * THANK YOU PLEASE SHIP UPS COLLECT, ACCT.# E87848 Net Order: Sales Tax: Freight: Order Total: 0.00 0.00 1,445.70 1,445.70 -Normal Carrier less than 100# UPS Collect E87848 -over 100# Please call for instructions -Purchase order number must be on all packing list, bill of ladings and invoices -Please contact buyer if you have any questions as  915-757-1300
# """


# Define a pattern for item lines
# This we would build based on user's input for their lines (assuming each line has consistant data)
ElPaso_pattern = [
    {"TEXT": {"REGEX": "\d{1,20}"}},  # Item code (1 to 20 digits)
    {"IS_SPACE": True, "OP": "*"},
    {"IS_ALPHA": True, "OP": "+"},  # Unit (e.g., EACH)
    {"IS_SPACE": True, "OP": "*"},
    {"IS_DIGIT": True, "OP": "+"},  # Quantity (whole number)
    {"IS_SPACE": True, "OP": "*"},
    {"TEXT": {"REGEX": "\.\d+"}, "OP": "+"},  # Unit cost decimal part (optional)
    {"IS_SPACE": True, "OP": "*"},
    {"TEXT": {"REGEX": "[,\.]?\d+"}, "OP": "+"}, # Amount decimal part (optional with comma or period)        
]
