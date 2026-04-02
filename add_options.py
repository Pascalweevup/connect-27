import re
import json

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace "Journée Délégués" with "Journée d'études"
    content = content.replace("Journée Délégués", "Journée d'études")

    # 2. Add options for Athens FNB
    athens_fnb_target = '''{ desc: "Soirée de Gala - Ble Pavillon - Option 1\\nMenu Option A", price: 28050.00, subDesc: "Apéritif & Canapé\\nEntrée\\nPlat principal\\nDessert\\nMignardises\\nCafé" },'''
    athens_fnb_replacement = athens_fnb_target + '''
                        { desc: "Soirée de gala - Ble Pavillon - Option 1\\nMenu Option B\\nQuantité: 300", price: 29700.00, isOption: true, subDesc: "Apéritif & Canapé\\nEntrée\\nPlat principal\\nDessert\\nMignardises\\nCafé" },
                        { desc: "Soirée de gala - Asteria Glyfada - Option 2\\nMenu Option A\\nQuantité: 300", price: 46563.00, isOption: true, subDesc: "Cocktail de bienvenue\\nApéritif\\nEntrée\\nPlat\\nDessert\\nDouceurs\\nCafé ou thé\\nTous les tarifs fournis sont basés sur l'année en cours. Notre partenaire estime une augmentation de 8 à 10% pour 2027." },
                        { desc: "Soirée de gala - Asteria Glyfada - Option 2\\nMenu Option B\\nQuantité: 300", price: 49485.00, isOption: true, subDesc: "Cocktail de bienvenue\\nApéritif\\nEntrée\\nPlat\\nDessert\\nDouceurs\\nCafé ou thé\\nTous les tarifs fournis sont basés sur l'année en cours. Notre partenaire estime une augmentation de 8 à 10% pour 2027." },'''
    content = content.replace(athens_fnb_target, athens_fnb_replacement)

    athens_fnb_target2 = '''{ desc: "F&B - Open Bar complet pendant 2 heures après le dîner", price: 7983.00, subDesc: "Whisky, Vodka, Gin, Rhum, Tequila" }'''
    athens_fnb_replacement2 = athens_fnb_target2 + ''',
                        { desc: "F&B - Bar à vin\\nQuantité: 300", price: 1656.00, isOption: true, subDesc: "Consommation illimitée toute la nuit\\nVin blanc, rouge et rose\\nEau minérale naturelle et gazeuse\\nBoissons sans alcool et jus\\nBière\\nTous les tarifs fournis sont basés sur l'année en cours. Notre partenaire estime une augmentation de 8 à 10% pour 2027." },
                        { desc: "F&B - Open Bar\\nQuantité: 300", price: 9315.00, isOption: true, subDesc: "Consommation illimitée\\nAperol Spritz, Paloma, Negroni\\nTous les tarifs fournis sont basés sur l'année en cours. Notre partenaire estime une augmentation de 8 à 10% pour 2027." }'''
    content = content.replace(athens_fnb_target2, athens_fnb_replacement2)

    # Athens Tech Staff
    athens_tech = '''{ desc: "Soirée de Gala\\nForfait technique + DJ", price: 4400.00, subDesc: "Scène\\nVidéo & son & Lumière\\nTechniciens sur place" },'''
    athens_tech_replacement = athens_tech + '''
                        { desc: "Soirée de Gala\\nForfait technique + DJ (Option 2)", price: 11099.00, isOption: true, subDesc: "Scène\\nVidéo & son & Lumière\\nTechniciens sur place" },'''
    content = content.replace(athens_tech, athens_tech_replacement)

    # Athens Project Team (and Malta Project team too!)
    pt_target = '''{ desc: "Taxe de résilience pour le changement climatique", price: 80.00 }'''
    pt_replacement = pt_target + ''',
                        { desc: "Calcul de l'empreinte carbone\\nSolution + 2 jours d'heures de travail", price: 3000.00, isOption: true, subDesc: "L'évaluation de l'empreinte carbone d'un événement vise à évaluer et rendre compte de son impact environnemental en termes d'émissions de gaz à effet de serre, et à prendre des mesures pour atténuer cet impact.\\nNotre solution Nous travaillons avec un partenaire de confiance spécialisé dans les évaluations carbone d'événements. Il nous fournit une interface conviviale pour consolider l'empreinte carbone d'un événement. Nous pouvons saisir toutes les informations relatives à la consommation d'énergie de toutes les parties prenantes impliquées dans votre séminaire (agence, fournisseurs, participants, etc.)" }'''
    content = content.replace(pt_target, pt_replacement)

    pt_target2 = '''{ desc: "Eco Taxe", price: 30.00 }'''
    pt_replacement2 = pt_target2 + ''',
                        { desc: "Calcul de l'empreinte carbone\\nSolution + 2 jours d'heures de travail", price: 3000.00, isOption: true, subDesc: "L'évaluation de l'empreinte carbone d'un événement vise à évaluer et rendre compte de son impact environnemental en termes d'émissions de gaz à effet de serre, et à prendre des mesures pour atténuer cet impact.\\nNotre solution Nous travaillons avec un partenaire de confiance spécialisé dans les évaluations carbone d'événements." }'''
    content = content.replace(pt_target2, pt_replacement2)


    # Athens Other
    athens_other = '''{ desc: "Cadeau pour l'équipe gagnante: Savons à l'huile d'olive grecque Organik", price: 247.50, subDesc: "frais de livraison non inclus\\nSavons Oliviada 100% naturels et faits à la main (2 unités) dans une boîte en bois" }'''
    athens_other_repl = athens_other + ''',
                        { desc: "Transferts aéroport - Option", price: 4290.00, isOption: true, subDesc: "Minivans 10-12 pers en rotation" },
                        { desc: "Team Building\\nOutdoor Living - SBS Studios - The Road to Blockbuster Success - Option 2", price: 26812.50, isOption: true },
                        { desc: "Transport - TB Option 2", price: 2000.00, isOption: true },
                        { desc: "Mosaïque Photo - Option", price: 1000.00, isOption: true }'''
    content = content.replace(athens_other, athens_other_repl)

    # Malta Venue
    malta_venue = '''{ desc: "Lieu de la Soirée de Gala - Montekristo Estate - Option 1\\nLocation de la salle", price: 3542.37, subDesc: "The Renaissance Hall" }'''
    malta_venue_repl = malta_venue + ''',
                        { desc: "Lieu de la Soirée de Gala - La Valette Hall - Option 2\\nLocation de la salle", price: 4070.00, isOption: true },
                        { desc: "Salles de sous-commission offertes - 5ème étage", price: 0, subDesc: "Offert\\nSalle de conseil - 6 pax" }'''
    content = content.replace(malta_venue, malta_venue_repl)

    # Malta FNB
    malta_fnb = '''{ desc: "F&B - Open Bar 4h", price: 3357.00, subDesc: "MK Wine, MK beer, MK soft drinks and water" }'''
    malta_fnb_repl = malta_fnb + ''',
                        { desc: "Soirée de Gala - La Valette HALL - Option 2\\nQuantité: 300", price: 20415.00, isOption: true, subDesc: "1 entrée\\n1 plat principal\\n1 dessert" },
                        { desc: "F&B - Verre de bienvenue Prosecco\\nQuantité: 300", price: 3993.00, isOption: true },
                        { desc: "F&B - Boissons Forfait vin local\\nQuantité: 300", price: 3564.00, isOption: true },
                        { desc: "F&B - Open Bar 2h\\nQuantité: 300", price: 2442.00, isOption: true }'''
    content = content.replace(malta_fnb, malta_fnb_repl)

    # Malta Tech & Staff
    malta_tech = '''{ desc: "Interprétation via IA - Acolad. - Option 1", price: 2629.00 },'''
    malta_tech_repl = malta_tech + '''
                        { desc: "Interprétation via interprète à distance - Acolad. - Option 2", price: 4829.00, isOption: true },'''
    content = content.replace(malta_tech, malta_tech_repl)

    malta_tech2 = '''{ desc: "Technique + DJ", price: 8211.50, subDesc: "Technique pour la cérémonie de remise des prix\\nScène, Vidéo, son, lumière" },'''
    malta_tech2_repl = malta_tech2 + '''
                        { desc: "Soirée de Gala - La Valette HALL - Option 2\\nSupport technique", price: 550.00, isOption: true, subDesc: "Éclairage d'ambiance" },
                        { desc: "Technique + DJ (Option 2)", price: 12685.00, isOption: true, subDesc: "Technique pour la cérémonie de remise des prix\\nScène, Vidéo, son, lumière" },
                        { desc: "Staff - Hôtesse", price: 396.00, isOption: true, subDesc: "Personnel de vestiaire : 4 hôtesses" },
                        { desc: "Staff - Sécurité", price: 247.50, isOption: true, subDesc: "3 agents de sécurité - 6 heures" },'''
    content = content.replace(malta_tech2, malta_tech2_repl)

    # Malta Sceno
    malta_sceno = '''{ desc: "Soirée de Gala\\nPhotocall", price: 396.00, subDesc: "3mx2m" }'''
    malta_sceno_repl = malta_sceno + ''',
                        { desc: "Soirée de Gala - La Valette Hall - Option 2\\nRideau rouge - option", price: 600.00, isOption: true }'''
    content = content.replace(malta_sceno, malta_sceno_repl)

    # Malta Other
    malta_other = '''{ desc: "Team Building\\nCadeau pour l'équipe gagnante: Pack huile d'olive extra vierge et vinaigre", price: 239.25, subDesc: "frais de livraison non inclus\\nCe pack souvenir comprend un goût d'huile d'olive extra vierge maltaise, 2 huiles facturées et un vinaigre infusé" }'''
    malta_other_repl = malta_other + ''',
                        { desc: "Transferts aéroport - Option\\nQuantité : 2", price: 2442.00, isOption: true, subDesc: "Rotation\\n25 vans x 6 pers\\n10 vans x 15 pers" },
                        { desc: "Transferts aéroport - Hôte à l'aéroport - Option\\nQuantité : 1", price: 180.00, isOption: true, subDesc: "Hôte/hôtesse pendant 3 heures" },
                        { desc: "Team Building\\nOutdoor Living - SBS Studios - The Road to Blockbuster Success - Option 2", price: 26812.50, isOption: true },
                        { desc: "Transport vers Mdina - TB Option 2", price: 2000.00, isOption: true },
                        { desc: "Mosaïque Photo - Option", price: 1000.00, isOption: true }'''
    content = content.replace(malta_other, malta_other_repl)

    # UI Modification
    old_span = '<span className="text-gray-900 font-bold whitespace-nowrap">{formatEur(item.price)}</span>'
    new_span = '''<span className={`text-gray-900 font-bold whitespace-nowrap ${item.isOption ? 'bg-amber-100 px-2 py-1 rounded text-amber-900 text-xs ml-2 border border-amber-200' : ''}`}>
                                                                {item.isOption 
                                                                    ? (item.price ? `En option (+ ${formatEur(item.price)})` : 'En option') 
                                                                    : (item.price === 0 ? 'Offert' : formatEur(item.price))}
                                                            </span>'''
    content = content.replace(old_span, new_span)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('/Users/lolaricharte/Documents/connect-27/index.html')
update_file('/Users/lolaricharte/Documents/connect-27/print.html')
