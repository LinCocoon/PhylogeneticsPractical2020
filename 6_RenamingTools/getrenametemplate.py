# Renames trees made from a known, constant set of ~30 entries

#run following lines if dict needs to change:

#alllines = []
#with open("oritemplate.txt", "r") as input_file:
#    alllines = input_file.read().splitlines()

#Dict = dict()
#for line in alllines:
#    Dict[str(line).split(" ")[0]] = (str(line).split(" ")[1])

#

def rename(file):
    Dict = {'GBDL00031': 'ADE_Noterus_clavicornis_BMNH1425090',
            'GBDL00072': 'ADE_Haliplus_lineatocollis',
            'GBDL00095': 'ADE_Omus_cazieri',
            'GBDL00140': 'ADE_Hydroporus_erythrocephalus',
            'GBDL00264': 'POLY_Elodes_minuta',
            'GBDL00388': 'ADE_Macrogyrus_oblongus',
            'GBDL00413': 'POLY_Aethina_tumida',
            'GBDL00420': 'ADE_Liopterus_haemorrhoidalis',
            'GBDL00466': 'POLY_Medon_piceus',
            'GBDL00570': 'POLY_Apatides_fortis',
            'GBDL00587': 'MYXO_Incoltorrida_madagassica',
            'GBDL00682': 'MYXO_Hydroscapha_granulum',
            'GBDL00701': 'POLY_Agrilus_planipennis',
            'GBDL00741': 'POLY_Nosodendron_fasciculare',
            'GBDL00755': 'UNCLASSIFIED_Coleoptera_sp._ctg072_ACP-2013',
            'GBDL00890': 'ARCH_Tetraphalerus_bruchi',
            'GBDL00931': 'POLY_Lymexylon_navale',
            'GBDL00948': 'POLY_Plateumaris_sericea',
            'GBDL01086': 'MYXO_Sphaerius_sp._BT0074',
            'GBDL01173': 'ADE_Aspidytes_niobe',
            'GBDL01224': 'POLY_Ips_sexdentatus',
            'GBDL01306': 'POLY_Heterocerus_fenestratus',
            'GBDL01312': 'POLY_Urodontus_glabratus',
            'GBDL01397': 'POLY_Dascillus_cervinus',
            'GBDL01407': 'ADE_Meru_phyllisae',
            'GBDL01463': 'POLY_Clambus_sp._CLA01',
            'GBDL01464': 'ARCH_Priacma_serrata',
            'GBDL01734': 'OUTGROUP_Corydalus_cornutus',
            'GBDL01738': 'OUTGROUP_Osmylus_fulvicephalus',
            'SPSO00024': 'ADE_Trechus_obtusus',
            'SPSO00040': 'POLY_Kissister_minimus',
            'SRAA00082': 'POLY_Rhinorhipus_tamborinensis',
            'SRAA00101': 'OUTGROUP_Subilla_sp._AD-2014'}
    
    with open(file, "r") as input_file:
        tree = str(input_file.read().splitlines()).strip("']").strip("['")

    for i in Dict.keys():
        tree = tree.replace(i, Dict[i])

    outF = open(f"{file}_renamed", "w")
    outF.write(tree)
