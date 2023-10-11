var newBuild = {

    "/pa/units/addon/demi_titan_bot/demi_titan_bot.json": ["factory", 0, { row: 0, column: 5 }],

    "/pa/units/addon/swordfish/swordfish.json": ["air", 0, { row: 2, column: 6 }],
    "/pa/units/addon/adv_stealth_transport/adv_stealth_transport.json": ["air", 0, { row: 1, column: 6 }],

    "/pa/units/addon/pounder/pounder.json": ["combat", 0, { row: 1, column: 5 }],
    "/pa/units/addon/anti_missile_tower/anti_missile_tower.json": ["combat", 0, { row: 0, column: 5 }],
    "/pa/units/addon/basic_missile_defence/basic_missile_defence.json": ["combat", 0, { row: 2, column: 5 }],

    "/pa/units/addon/andreas/andreas.json": ["orbital", 0, { row: 2, column: 5 }],

    "/pa/units/addon/orbital_anti_nuke/orbital_anti_nuke.json": ["orbital_structure", 6, { row: 0, column: 0 }],

    "/pa/units/addon/fabrication_sub/fabrication_sub.json": ["sea", 0, { row: 2, column: 7 }],
    "/pa/units/addon/naval_anti_orbital_ship/naval_anti_orbital.json": ["sea", 0, { row: 2, column: 6 }],

    "/pa/units/addon/hover_fab/hover_fab.json": ["vehicle", 9, { row: 2, column: 8 }],
    "/pa/units/addon/stalker/stalker.json": ["vehicle", 9, { row: 1, column: 6 }],
    "/pa/units/addon/adv_tank_hover/adv_tank_hover.json": ["vehicle", 9, { row: 1, column: 5 }],

    "/pa/units/land/bot_aa/bot_aa.json": ["bot", 0, { row: 2, column: 6 }],
    "/pa/units/addon/rex/rex.json": ["bot", 0, { row: 2, column: 7 }],
    "/pa/units/addon/adv_heavy_bot/adv_heavy_bot.json": ["bot", 0, { row: 1, column: 6 }],

    "/pa/units/addon/metal_generator/metal_generator.json": ["utility", 0, { row: 1, column: 5 }],
    "/pa/units/addon/adv_metal_generator/adv_metal_generator.json": ["utility", 0, { row: 0, column: 5 }],
    "/pa/units/addon/adv_energy_storage/adv_energy_storage.json": ["utility", 0, { row: 1, column: 6 }],
    "/pa/units/addon/jammer_titan/jammer_titan.json": ["utility", 0, { row: 1, column: 0 }],
    "/pa/units/addon/system_radar/system_radar.json": ["utility", 0, { row: 0, column: 2 }],
    "/pa/units/addon/adv_metal_storage/adv_metal_storage.json": ["utility", 0, { row: 0, column: 6 }],
    "/pa/units/addon/jammer/jammer.json": ["utility", 0, { row: 2, column: 6 }],

    "/pa/units/addon/fab_tower/fab_tower.json": ["factory", 0, { row: 2, column: 5 }],
    "/pa/units/addon/adv_fab_tower/adv_fab_tower.json": ["factory", 0, { row: 1, column: 5 }],

    "/pa/units/l_addon/mass_generator/mass_generator.json": ["L_utility", 0, { row: 1, column: 5, titans: true }],
    "/pa/units/l_addon/adv_mass_generator/adv_mass_generator.json": ["L_utility", 0, { row: 0, column: 5, titans: true }],
    "/pa/units/l_addon/system_radar/system_radar.json": ["L_utility", 0, { row: 0, column: 2 }],
    "/pa/units/l_addon/l_jammer_station/l_jammer_station.json": ["L_utility", 0, { row: 0, column: 6 }],
    "/pa/units/l_addon/basic_missile_defence/basic_missile_defence.json": ["L_combat", 0, { row: 2, column: 5 }],

    "/pa/units/l_addon/anti_orbital_armor/lynx.json": ["L_vehicle", 0, { row: 2, column: 6, titans: true }],

    "/pa/units/l_addon/anti_orbital_ship/anti_orbital_ship.json": ["L_sea", 0, { row: 2, column: 5 }],

    "/pa/units/l_addon/anti_ground_satellite/almaz.json": ["L_orbital", 0, { row: 2, column: 5 }],

    "/pa/units/l_addon/l_orbital_jammer/l_orbital_jammer.json": ["L_orbital_structure", 0, { row: 1, column: 1 }],
    "/pa/units/l_addon/l_orbital_power/l_orbital_power.json": ["L_orbital_structure", 0, { row: 1, column: 2 }],
    "/pa/units/l_addon/orbital_anti_nuke/orbital_anti_nuke.json": ["L_orbital_structure", 6, { row: 1, column: 3 }],

    "/pa/units/l_addon/l_demi_titan_bot/l_demi_titan_bot.json": ["L_factory", 0, { row: 0, column: 5 }],

    "/pa/units/l_addon/fab_turret/fab_turret.json": ["L_factory", 0, { row: 2, column: 5, titans: true }],
    "/pa/units/l_addon/adv_fab_turret/adv_fab_turret.json": ["L_factory", 0, { row: 1, column: 5, titans: true }],


    "/pa/units/b_addon/basic_missile_defence/basic_missile_defence.json": ["bug_combat", 0, { row: 2, column: 5 }],
    "/pa/units/b_addon/metal_generator/metal_generator.json": ["bug_utility", 0, { row: 1, column: 5 }],
    "/pa/units/b_addon/adv_metal_generator/adv_metal_generator.json": ["bug_utility", 0, { row: 0, column: 5 }],
    "/pa/units/b_addon/system_radar/system_radar.json": ["bug_utility", 0, { row: 2, column: 5 }],
    "/pa/units/b_addon/fab_tower/fab_tower.json": ["bug_factory", 0, { row: 2, column: 5 }],
    "/pa/units/b_addon/adv_fab_tower/adv_fab_tower.json": ["bug_factory", 0, { row: 1, column: 5 }]


}
if (Build && Build.HotkeyModel && Build.HotkeyModel.SpecIdToGridMap) {
    _.extend(Build.HotkeyModel.SpecIdToGridMap, newBuild);
}