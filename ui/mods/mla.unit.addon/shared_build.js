var newBuild = {
    "/pa/units/addon/swordfish/swordfish.json": ["air", 0, { row: 2, column: 6 }],

    "/pa/units/addon/pounder/pounder.json": ["combat", 0, { row: 1, column: 5 }],
    "/pa/units/addon/anti_missile_tower/anti_missile_tower.json": ["combat", 0, { row: 0, column: 5 }],

    "/pa/units/addon/andreas/andreas.json": ["orbital", 9, { row: 2, column: 5 }],

    "/pa/units/addon/stalker/stalker.json": ["vehicle", 9, { row: 1, column: 6 }],

    "/pa/units/addon/rex/rex.json": ["bot", 9, { row: 2, column: 6 }],

    "/pa/units/addon/metal_generator/metal_generator.json": ["utility", 0, { row: 1, column: 5 }],
    "/pa/units/addon/adv_metal_generator/adv_metal_generator.json": ["utility", 0, { row: 0, column: 5 }],
    "/pa/units/addon/solar_cell/solar_cell.json": ["utility", 0, { row: 2, column: 5 }],
}
if (Build && Build.HotkeyModel && Build.HotkeyModel.SpecIdToGridMap) {
    _.extend(Build.HotkeyModel.SpecIdToGridMap, newBuild);
}