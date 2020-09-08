var newBuild = {
    "/pa/units/addon/swordfish/swordfish.json": ["air", 0, { row: 2, column: 6 }],
    "/pa/units/addon/adv_stealth_transport/adv_stealth_transport.json": ["air", 0, { row: 1, column: 6 }],

    "/pa/units/addon/pounder/pounder.json": ["combat", 0, { row: 1, column: 5 }],
    "/pa/units/addon/anti_missile_tower/anti_missile_tower.json": ["combat", 0, { row: 0, column: 5 }],

    "/pa/units/addon/andreas/andreas.json": ["orbital", 0, { row: 2, column: 5 }],

    "/pa/units/addon/anti_sub_ship/anti_sub_ship.json": ["sea", 0, { row: 2, column: 7 }],
    "/pa/units/addon/naval_anti_orbital_ship/naval_anti_orbital.json": ["sea", 0, { row: 2, column: 6 }],

    "/pa/units/addon/stalker/stalker.json": ["vehicle", 9, { row: 1, column: 6 }],
    "/pa/units/addon/adv_tank_hover/adv_tank_hover.json": ["vehicle", 9, { row: 1, column: 5 }],

    "/pa/units/addon/rex/rex.json": ["bot", 0, { row: 2, column: 6 }],
    "/pa/units/addon/bot_aa/bot_aa.json": ["bot", 0, { row: 2, column: 7 }],
    "/pa/units/addon/adv_heavy_bot/adv_heavy_bot.json": ["bot", 0, { row: 1, column: 6 }],

    "/pa/units/addon/metal_generator/metal_generator.json": ["utility", 0, { row: 1, column: 5 }],
    "/pa/units/addon/adv_metal_generator/adv_metal_generator.json": ["utility", 0, { row: 0, column: 5 }],
    "/pa/units/addon/adv_metal_storage/adv_metal_storage.json": ["utility", 0, { row: 0, column: 6 }],
    "/pa/units/addon/adv_energy_storage/adv_energy_storage.json": ["utility", 0, { row: 1, column: 6 }],
    "/pa/units/addon/solar_cell/solar_cell.json": ["utility", 0, { row: 2, column: 5 }],

    "/pa/units/addon/fab_tower/fab_tower.json": ["factory", 0, { row: 2, column: 5 }],
    "/pa/units/addon/adv_fab_tower/adv_fab_tower.json": ["factory", 0, { row: 1, column: 5 }],

    "/pa/units/l_addon/mass_generator/mass_generator.json": ["L_utility", 0, { row: 1, column: 5, titans: true }],
    "/pa/units/l_addon/adv_mass_generator/adv_mass_generator.json": ["L_utility", 0, { row: 0, column: 5, titans: true }]
}
if (Build && Build.HotkeyModel && Build.HotkeyModel.SpecIdToGridMap) {
    _.extend(Build.HotkeyModel.SpecIdToGridMap, newBuild);
}