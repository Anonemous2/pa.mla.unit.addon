


	
	function doCommand(world, id, planet, usedIdArray){ 
		
	
		var two = !_.isArray(id);
				if (two){
						id = [id];
				}

        if (world){ 

            return world.getUnitState(id).then(function (ready) {
				var unitData = this.result;
				var one = !_.isArray(unitData);
				if (one){
						unitData = [unitData];
				}
			
				
				for(var i = 0; i<unitData.length;i++){
				
					
						
						
					if(_.contains(usedIdArray,id[i]) !== true){
						
							if (unitData[i].built_frac == undefined){
									
									
							
										api.getWorldView(0).sendOrder({units: id[i],command: 'patrol',location: {planet: unitData[i].planet,pos: unitData[i].pos},queue: false})
										
										usedIdArray.push(id[i])
										
							}	
											
				}	
						
							
				}
		
				return usedIdArray;
				
				
				
			});
			
		
		
        }
		else
		{
			return
		
		}
	};
	
	var idArray = [];
	var advancedIdArray = [];
	var legionIdArray = [];
	var advancedLegionIdArray = [];
	var chosenPlanet = 0;
	var automation = function () { 
		
        var worldView = api.getWorldView(0);
		var armyindex = model.armyIndex();
		if (typeof armyindex == "undefined"){
			
			armyindex = model.armyId()
		}
		
		

	
        if (worldView) {
			if(model){
				var planets = model.planetListState()
				for(planet in planets.planets){
					planet = planets.planets[planet]
					if(planet.id !== undefined || planet.id === 0){
						chosenPlanet = planet.index;
						
						worldView.getArmyUnits(armyindex,chosenPlanet).then(function (ready) {
			
							var army = this.result
			
						
							if (army.hasOwnProperty('/pa/units/addon/adv_fab_tower/adv_fab_tower.json')) {
								doCommand(worldView, army['/pa/units/addon/adv_fab_tower/adv_fab_tower.json'], chosenPlanet, advancedIdArray).then(function (result) { advancedIdArray = result })
							}
							if (army.hasOwnProperty('/pa/units/addon/fab_tower/fab_tower.json')) {
								doCommand(worldView, army['/pa/units/addon/fab_tower/fab_tower.json'], chosenPlanet, idArray).then(function (result) { idArray = result })
							}
							if (army.hasOwnProperty('/pa/units/l_addon/adv_fab_turret/adv_fab_turret.json')) {
								doCommand(worldView, army['/pa/units/l_addon/adv_fab_turret/adv_fab_turret.json'], chosenPlanet, advancedLegionIdArray).then(function (result) { advancedLegionIdArray = result })
							}
							if (army.hasOwnProperty('/pa/units/l_addon/fab_turret/fab_turret.json')) {
								doCommand(worldView, army['/pa/units/l_addon/fab_turret/fab_turret.json'], chosenPlanet, legionIdArray).then(function (result) { legionIdArray = result })
							}
							if (army.hasOwnProperty('/pa/units/b_addon/adv_fab_tower/adv_fab_tower.json')) {
								doCommand(worldView, army['/pa/units/b_addon/adv_fab_tower/adv_fab_tower.json'], chosenPlanet, advancedIdArray).then(function (result) { advancedIdArray = result })
							}
							if (army.hasOwnProperty('/pa/units/b_addon/fab_tower/fab_tower.json')) {
								doCommand(worldView, army['/pa/units/b_addon/fab_tower/fab_tower.json'], chosenPlanet, idArray).then(function (result) { idArray = result })
							}
							
						});
	
	
	
	
					}
	
				}
			}
            
			_.delay(automation, 5000); // effectivly acts as a loop, this is the time between loops
        }
        else
            _.delay(automation, 5000);
    };
	
	
    automation();
	
				//if (typeof initialData == "undefined" ){ initialData = unitData;} way to set the first time you got data
				//world.sendOrder({units:id,command: 'assist',location : {entity: 5268, world: 0}})
				//if (typeof initialarmy == "undefined" ){ initialarmy = army;}



