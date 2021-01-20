

(function() {
	
	function doCommand(world, id, command, usedIdArray){ 
		
		
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
									
									
							
										api.getWorldView(0).sendOrder({units: id[i],command: 'patrol',location: {planet: 0,pos: unitData[i].pos},queue: false})
										
										usedIdArray.push(id[i])
										
							}	
											
				}	
						
							
				}
		
				return usedIdArray;
				
				
				
			});
			
		
		
        }
		else
		{
			_.delay(automation, 1000);
		
		}
	};
	
	var idArray = [];
	var advancedIdArray = [];
	var legionIdArray = [];
	var advancedLegionIdArray = [];
	var automation = function () { 
	
        var worldView = api.getWorldView(0);
		var armyindex = model.armyIndex();
		if (typeof armyindex == "undefined"){
			
			armyindex = model.armyId()
		}
		
        if (worldView) {
            worldView.getArmyUnits(armyindex,0).then(function (ready) {
			
				var army = this.result
				
			
				if(army.hasOwnProperty('/pa/units/addon/adv_fab_tower/adv_fab_tower.json')){
				doCommand(worldView, army['/pa/units/addon/adv_fab_tower/adv_fab_tower.json'], 'patrol',advancedIdArray).then(function(result){advancedIdArray = result})
				
				}
				if(army.hasOwnProperty('/pa/units/addon/fab_tower/fab_tower.json')){
				doCommand(worldView, army['/pa/units/addon/fab_tower/fab_tower.json'], 'patrol',idArray).then(function(result){idArray = result})
				}
				if(army.hasOwnProperty('/pa/units/l_addon/adv_fab_turret/adv_fab_turret.json')){
					doCommand(worldView, army['/pa/units/l_addon/adv_fab_turret/adv_fab_turret.json'], 'patrol',advancedLegionIdArray).then(function(result){advancedLegionIdArray = result})
					}
				if(army.hasOwnProperty('/pa/units/l_addon/fab_turret/fab_turret.json')){
					doCommand(worldView, army['/pa/units/l_addon/fab_turret/fab_turret.json'], 'patrol',legionIdArray).then(function(result){legionIdArray = result})
					}
                
			});
			_.delay(automation, 5000);
        }
        else
            _.delay(automation, 5000);
    };
	
	
    automation();
	
})();


