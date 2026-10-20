
# ImagineYourCraft feature inventory

Complete inventory of the ImagineYourCraft (IYC) mod for Minecraft 1.8, as shipped by `Launcher-IYC-5.1` (`.iyc/libs/minecraft.jar`, a patched 1.8 client), and what the datapack does with each entry on Minecraft 26.3.

Every value below comes from the decompiled jar (block registry `a`, item registry `dm_2`, recipes `iu_1`, furnace recipes `it_1`, compression recipes `iv_1`, overworld decorator `td_1`, Nether generator `um_2`, behaviour classes named in each section) and from its assets (`assets/iyc/lang`, `blockstates`, `models`, `textures`, the launcher asset index for sounds).

## Status legend

| Status | Meaning |
|---|---|
| Implemented | Works in the datapack with the original stats and behaviour, or the closest one 26.3 allows (the compromise is written next to it) |
| Partial | Present, but part of the original behaviour is missing (written next to it) |
| Vanilla | Minecraft 26.3 has its own equivalent, the datapack uses or points to it |
| Missing | Not in the datapack, with the reason |
| Out of scope | Belongs to the launcher, the client or the server plugins, not to a datapack |
| Unfinished | Declared by the mod (lang entry, texture or constant) but never registered, so it never existed in game |
| Extra | Not in the original mod, added by the datapack author |

Conventions: hardness / resistance are the raw values given to `setHardness` / `setResistance` in 1.8, `light 15` is `setLightLevel(1.0)`. Creative tabs of the mod: IYC blocks, IYC decoration blocks, IYC materials, IYC tools, IYC combat, IYC food. Ids are the registry names (`iyc:<name>`), meta values are the variant index.

## 1. World generation

| Feature | Original (class) | Datapack | Status |
|---|---|---|---|
| Ruby ore | `td_1`: 1 vein of 6 per chunk, y 0 to 12 | Deepslate ruby ore, 36 veins per 96x96 region (one per chunk), y -64 to -52 (the 1.8 bottom of the world mapped onto the 26.3 one) | Implemented |
| Sapphire ore | 1 vein of 7 per chunk, y 0 to 13 | Deepslate sapphire ore, 36 veins per region, y -64 to -51 | Implemented |
| Topaz ore | 1 vein of 5 per chunk, y 0 to 11 | Deepslate topaz ore, 36 veins per region, y -64 to -53 | Implemented |
| Adamantium ore | 1 vein of 4 per chunk, y 0 to 9 | Deepslate adamantium ore, 36 veins per region, y -64 to -55 | Implemented |
| Slate ore | 10 veins of 12 per chunk, y 60 to 128 | 360 veins per region, y 60 to 128 | Implemented |
| Steel ore | `um_2` with `hf_2` / `hg_2`: Nether, glowstone-like clusters hanging under netherrack ceilings (rand(rand(10)+1) tries at y 4-124 plus 10 tries at y 0-128 per chunk, 1500 placements each) | Nether, ore placed in air directly under netherrack, 72 clusters per region, y 4 to 124 | Implemented (smaller clusters than the 1500-try glowstone algorithm) |
| Lignite ore | `um_2` with `hj_2` / `hk_2`: same as steel | Same as steel | Implemented |
| Blue, white and black flowers | `td_1`: each vanilla flower attempt has a 1/4 chance per custom flower to also place a patch of it | Grass surface patches, 18 per region per flower | Implemented |
| Cherry trees | Patched vanilla `log2` / `leaves2` / `sapling` with a cherry variant (`bj_0.CHERRY`) | 26.3 cherry trees and cherry groves | Vanilla |
| Cherry from cherry leaves | `bn`: cherry leaves drop a cherry like dark oak leaves drop apples (1/200, fortune raises it) | `minecraft:blocks/cherry_leaves` loot table also drops the IYC cherry with the vanilla apple chances | Implemented |
| Ore drops and experience | `gz_2`: XP 3-6 for ruby, sapphire, topaz and adamantium ores, 2-5 lignite, 3-5 slate, steel ore drops itself | Custom ores drop their gem, fragment, slate or lignite with the same experience (StewBeet `NoSilkTouchDrop.experience`), steel ore drops raw steel and no experience | Implemented |
| Ore harvest level | `er_2`: gem, steel, slate and adamantium ores and storage blocks need an iron pickaxe, lignite ore any pickaxe | StewBeet `Mining(level="iron")`: storage blocks stand on vanilla blocks of the iron level (diamond, gold, raw gold and emerald blocks), which drop nothing to a weaker pickaxe at vanilla speed; the ores keep the ore host, so their item and experience vanish when the nearest survival player within 8 blocks breaks them with anything but an iron, diamond or netherite pickaxe | Implemented (ores break at the speed of polished deepslate) |

## 2. Materials

| Id | French / English name | Datapack id | Notes | Status |
|---|---|---|---|---|
| `rubis` | Rubis / Ruby | `ruby` | Ore drop, smelted from ruby ore (XP 0.6) | Implemented |
| `saphir` | Saphir / Sapphire | `sapphire` | Ore drop, smelted from ore (XP 0.6) | Implemented |
| `topaze` | Topaze / Topaz | `topaz` | Ore drop, smelted from ore (XP 0.6) | Implemented |
| `adamantium_fragment` | Fragment d'adamantium | `adamantium_fragment` | Ore drop, smelted from ore (XP 0.4) | Implemented |
| `lignite` | Lignite | `lignite` | Ore drop, used by the lignite torch and its block. The author's notes call it a better coal, but neither the mod nor the datapack makes it a fuel | Implemented |
| `slate_item` | Ardoise / Slate | `slate` | Ore drop | Implemented |
| `steel_ingot` | Lingot d'acier / Steel ingot | `steel_ingot` | Smelted from steel ore (XP 0.4) | Implemented |
| `obsidian_ingot` | Lingot d'obsidienne | `obsidian_ingot` | Smelted from vanilla obsidian (XP 0.25) | Implemented |
| `steel_stick` | Baton en acier | `steel_stick` | 2 steel ingots vertical, x4 | Implemented |
| `stone_stick` | Baton en pierre | `stone_stick` | 3 stone in a diagonal, x4 | Implemented |
| `maille` | Mailles / Mesh | `chainmail` | 2 iron ingots vertical, x6 (the mod has no recipe using it; the datapack crafts vanilla chainmail armor with it) | Implemented |
| `hops`, `hops_seeds` | Houblon, Graines de houblon | `hops`, `hops_seeds` | See crops | Implemented |
| `cafeine`, `cola`, `taurine` | Cafeine, Cola, Taurine | `caffeine`, `cola`, `taurine` | Drink ingredients. The mod has no source for cola and taurine besides the creative tab; the author notes make them drop from wheat and sugar cane | Implemented (author notes) |
| `canette` | Canette vide / Empty can | `can` | `X X / X X / _X_` iron ingots, x4 | Implemented |
| `choppe` | Chope de biere / Mug | `beer_mug` | `# # / # # / ###` glass, x4 | Implemented |
| `empty_glass` | Verre / Glass | `empty_glass` | `# # / # # / _#_` glass, x4 | Implemented |
| Raw steel, steel nugget, steel dust, raw steel block, glass pot | | | Datapack additions around steel and nutella | Extra |

## 3. Storage blocks (`storage_block`, class `hf_1`, hardness 5, resistance 10, metal sound)

Recipe for each: 9 items in a 3x3 square, and back to 9 items (`iv_1`).

| Meta | Name | Item | Datapack id | Status |
|---|---|---|---|---|
| 0 | Bloc de rubis | ruby | `ruby_block` | Implemented |
| 1 | Bloc de topaze | topaz | `topaz_block` | Implemented |
| 2 | Bloc de saphir | sapphire | `sapphire_block` | Implemented |
| 3 | Bloc de lignite | lignite | `lignite_block` | Implemented |
| 4 | Bloc d'acier | steel ingot | `steel_block` | Implemented |
| 5 | Bloc massif d'obsidienne | obsidian ingot | `massive_obsidian_block` | Implemented |
| 6 | Bloc d'ardoise | slate | `slate_block` | Implemented |
| 7 | Bloc d'adamantium | adamantium fragment | `adamantium_block` | Implemented |

## 4. Ores (class `gz_2`, hardness 3, resistance 5)

| Id | Name | Drop | Datapack | Status |
|---|---|---|---|---|
| `rubis_ore` | Minerai de rubis | ruby | `ruby_ore`, `deepslate_ruby_ore` | Implemented |
| `saphir_ore` | Minerai de saphir | sapphire | `sapphire_ore`, `deepslate_sapphire_ore` | Implemented |
| `topaze_ore` | Minerai de topaze | topaz | `topaz_ore`, `deepslate_topaz_ore` | Implemented |
| `adamantium_ore` | Minerai d'adamantium | adamantium fragment | `adamantium_ore`, `deepslate_adamantium_ore` | Implemented |
| `steel_ore` | Minerai d'acier | itself | `steel_ore`, drops raw steel | Implemented |
| `lignite_ore` | Minerai de lignite | lignite | `lignite_ore` | Implemented |
| `slate_ore` | Minerai d'ardoise | slate | `slate_ore` | Implemented |

## 5. Tools (classes `fk_1` sword, `fi_2` shovel, `er_2` pickaxe, `dx_2` axe, `ee_2` hoe, tiers `dq_2`)

1.8 damage is the tier bonus plus 4 (sword), 3 (axe), 2 (pickaxe), 1 (shovel). The datapack starts from the 26.3 diamond tool and adds the difference to diamond (bonus 3.0, speed 8, enchantability 10).

| Tier | Durability | Mining speed | Damage bonus | Enchantability | Datapack (diamond + delta) | Status |
|---|---|---|---|---|---|---|
| EMERAUDE (emerald) | 1405 | 7.0 | 2.5 | 15 | durability 1405, damage -0.5, mining efficiency -1, enchantable 15 | Implemented |
| SAPHIR (sapphire) | 1639 | 9.0 | 3.25 | 8 | durability 1639, damage +0.25, mining efficiency +1, enchantable 8 | Implemented |
| RUBIS (ruby) | 1717 | 10.0 | 3.5 | 8 | durability 1717, damage +0.5, mining efficiency +2, enchantable 8 | Implemented |
| TOPAZE (topaz) | 1795 | 11.0 | 3.75 | 6 | durability 1795, damage +0.75, mining efficiency +3, enchantable 6 | Implemented |
| ADAMANTIUM | 1873 | 12.0 | 4.0 | 6 | durability 1873, damage +1, mining efficiency +4, enchantable 6 | Implemented |
| BAGUETTE (wands) | 2000 | 2.0 | 0 | 14 | see special items | Implemented |
| Obsidian and steel tools | not registered (obsidian textures and lang exist, no item) | Datapack tiers | Extra |

Each tier has sword, shovel, pickaxe, axe and hoe, crafted with the vanilla shapes and sticks.

## 6. Armor (class `dt_2`, tiers `dv_2`)

1.8 durability is the factor times 11 / 16 / 15 / 13 (helmet, chestplate, leggings, boots), the same formula 26.3 uses.

| Tier | Factor | Armor (helmet, chest, legs, boots) | Enchantability | Datapack | Status |
|---|---|---|---|---|---|
| Emerald | 26 | 3, 7, 5, 3 | 15 | durability 286 / 416 / 390 / 338, diamond armor minus 1 on chest and legs, toughness 2 | Implemented |
| Sapphire | 40 | 3, 8, 6, 3 | 8 | 440 / 640 / 600 / 520 | Implemented |
| Ruby | 46 | 3, 8, 6, 3 | 8 | 506 / 736 / 690 / 598 | Implemented |
| Topaz | 53 | 4, 8, 6, 4 | 6 | 583 / 848 / 795 / 689 | Implemented |
| Adamantium | 59 | 4, 8, 6, 4 | 6 | 649 / 944 / 885 / 767 | Implemented |
| Obsidian and steel armor | not registered | Datapack tiers | Extra |
| Chainmail from mesh | no recipe in the mod | `chainmail` crafts the vanilla chainmail pieces | Extra (author notes) |

The 26.3 toughness of 2 is kept from the diamond base, 1.8 had no toughness.

## 7. Weapons and special items

| Id | Name | Original behaviour | Datapack | Status |
|---|---|---|---|---|
| `crossbow` (`hu_2`) | Arbalete | Bow subclass, durability 199, needs bolts (or Infinity / creative), fires only after a 50 tick charge, bolt speed 3.0 at full charge (bow 2.0), crits at full charge, Power, Punch, Flame, Infinity work | `crossbow`, a vanilla crossbow with 199 durability and the mod's pulling textures, drawn in 50 ticks by its hidden `Heavy Draw` curse (StewBeet `RangedWeapon`), showing its fully drawn texture while loaded, loading bolts only (anything else is given back) and shooting them with x1.5 damage | Partial (26.3 crossbow rules: it loads, then fires on the next use) |
| `bolt` (entity `hd_2`) | Carreau | Arrow with base damage 3.0 (arrow 2.0) | `bolt`, the only ammunition of the crossbow, which multiplies the damage of what it shoots by 1.5 | Implemented |
| `baguette_bleue`, `_rouge`, `_violette`, `_jaune`, `_verte`, `_orange` (`fl_1`) | Baguettes (wands) | Tool items with no effective block, stack 1, durability 2000, lose 2 durability per hit, used by server plugins | Six wand items with 2000 durability | Implemented (no plugin behaviour) |
| `tournevis` (`fl_1`) | Tournevis sonic | Same wand class | `screwdriver`, 2000 durability | Implemented (no plugin behaviour) |
| `L118A`, `SW1911` (`fl_1`) | Guns | Same wand class, the shooting lived in a server plugin | `l118a`, `sw1911`, 2000 durability, the datapack recipes | Partial (no shooting, the plugin was not shipped) |
| `pokeball` | Pokeball | Plain item, server plugin item | `pokeball` | Implemented (no plugin behaviour) |
| `piece` | Monnaie / Money | Plain item, server currency | `coin` | Implemented |
| `hns_item` | Hide and seek item | Plain item, no creative tab, server minigame | `hns_item` | Implemented (no plugin behaviour) |
| `hidden_door_item` | Porte cachee | Constant and texture only, never registered | | Unfinished |
| `whiteFlag`, `blueFlag`, `redFlag` | Flags | English lang entries only | | Unfinished |
| Helice hat, reindeer antlers | `ib_1`, `hz_2`: cosmetic layers drawn on players the server granted them to | `helice_hat`, a hat item lowering gravity | Extra (inspired by the cosmetic) |
| Quiver, rock, old ruby, blank | | Datapack items | Extra |

## 8. Foods and drinks (`eb_2` food, `ht_2` drink)

Modern saturation is hunger x modifier x 2. `ht_2` passes its modifier to nowhere, so every drink keeps the default 0.6. Drinks stack to 1, are always edible, use the drink animation and give back their container. Every effect lasts 30 s at level I.

| Id | Name | Hunger | Saturation (26.3) | Effect | Container | Recipe | Status |
|---|---|---|---|---|---|---|---|
| `biere` | Biere | 8 | 9.6 | Nausea | beer mug | shapeless mug + hops | Implemented |
| `chocolat_chaud` | Chocolat chaud | 6 | 7.2 | Speed | can (the code returns a can for every drink except beer and apple juice) | `X#X / _X_` glass and cocoa beans | Implemented |
| `coca` | Coca | 6 | 7.2 | Haste | can | shapeless caffeine + cola + can | Implemented |
| `redbull` | RedBull | 5 | 6.0 | Regeneration | can | shapeless taurine + caffeine + can | Implemented |
| `apple_juice` | Jus de pomme | 4 | 4.8 | Jump boost | empty glass | shapeless empty glass + apple | Implemented |
| `tartine` | Tartine | 2 | 4.0 | | | `###` bread, x4 | Implemented |
| `nutella` | Nutella | 10 | 20.0 | | | `X X / X#X / _X_` glass and cocoa beans | Implemented |
| `tartine_nutella` | Tartine au nutella | 14 | 28.0 | | | nutella over toast, x2 | Implemented |
| `cherry` | Cerise | 3 | 6.0 | | | from cherry leaves | Implemented |
| `cherry_cake` (`gi_1`, item `cherry_cake_item`) | Gateau a la cerise | cake slices (7 bites) | | | | cherry over cake | Implemented |

## 9. Crops

| Id | Original | Datapack | Status |
|---|---|---|---|
| `hops_crops` (`gl_1`) | Wheat-like crop on farmland, 8 stages. Fully grown: drops hops, and 1 time in 6 caffeine instead; not grown: hops seeds | `hops_seeds` growing seed on farmland with the 8 stage textures, harvest drops hops with a 1/6 chance of caffeine instead | Implemented |
| Taurine from sugar cane, cola from wheat | Author notes | Common Signals item replacement (10 percent) | Extra (author notes) |

## 10. Music discs (`hw_2`, sounds in `iyc/sounds/records/*.ogg` of the asset index)

| Id | Artist, title | Sound | Status |
|---|---|---|---|
| `record_take_back_night` | CaptainSparklez, Take Back the Night | backnight | Implemented |
| `record_zombies` | Lokoise, Tous les zombies | zombies | Implemented |
| `record_chunks` | Lokoise, Bug de chunks | chunk | Implemented |
| `record_creep` | Lokoise, J'aime le creep' | creep | Implemented |
| `record_nofragays` | Lokoise, Le journal d'un naufragay | journal | Implemented |
| `record_sean_kevin` | Lokoise, J'suis Sean Kevin | kevin | Implemented |
| `record_give` | Lokoise, Je me give | give | Implemented |
| `record_pelles` | Lokoise, J'fais des pelles en diam's | pelles | Implemented |
| `record_geek` | Lokoise, J'geek un max | geek | Implemented |
| `record_acta` | Lokoise, ACTA | acta | Implemented |
| `record_hit` | Hit du moment | momenthit | Implemented |
| `record_touch` | Gunther, You touch my tralala | touch | Implemented |
| `record_mc_style` | CaptainSparklez, Minecraft Style | mcstyle | Implemented |
| `record_bouge` | GuzzProduction, Bouge Ton Cube | bouge | Implemented |
| `record_mauvaise` | ReAperr & MrElvilia, Mauvaise Idee | mauvaise | Implemented |
| `record_sfr` | Lokoise, Un debit tout pourri | debitSFR | Implemented |
| `record_revenge` | CaptainSparklez, Revenge | revenge | Implemented |
| `record_fallen_kingdom` | CaptainSparklez, Fallen Kingdom | fallenkingdom | Implemented |
| `record_tnt` | CaptainSparklez, TNT | tnt | Implemented |
| `record_gaga_outai` | TheDudesCraft, GAGAOUTAI | gagaoutai | Implemented |
| `record_the_miner` | AntVenom, The Miner | theminer | Implemented |
| `record_dont_mine_at_night` | BebopVox, Don't Mine At Night | mineatnight | Implemented |
| `record_girl_crafty` | TryHardNinja, That Girl is Crafty | girlcrafty | Implemented |
| `record_your_radio`, `record_thelan` | Your Radio and thelan Radio, Live | web radio streams (`http://music.servme.fr:8000/iyc`) | Out of scope (streams, dead servers) |
| `records.monstercat`, `records.nyancat` | Sound events without a disc item | | Unfinished |

The mod has no recipe for its discs (creative tab only). The datapack keeps them obtainable the StewBeet way (manual, commands).

## 11. Building blocks

### 11.1 Full blocks

| Id (meta) | Name | Stats | Behaviour, model | Recipe | Datapack | Status |
|---|---|---|---|---|---|---|
| `reversed_planks` 0-6 (`bi_0`) | Planches renversees (oak, spruce, birch, jungle, acacia, dark oak, cherry) | hardness 2, resistance 5, wood | Planks texture rotated 90 degrees on every face (`cube_90_all`) | 2 logs side by side, x8 | 7 blocks on the matching vanilla planks | Implemented |
| `step_block` | Bloc en dalles | hardness 4, resistance 10, rock | Smooth stone slab top texture on every face | 9 smooth stone slabs, x5 | Block on smooth stone | Implemented |
| `clear_glass` (`ae_0`) | Verre d'IYC (ancient glass) | hardness 0.3, glass | Glass: cutout, drops nothing without silk touch | none (the datapack keeps its own 9 glass into 4) | Block on vanilla glass | Implemented |
| `transparent_light_block` (`hj_1`) | Bloc transparent eclairant | hardness 0.5, resistance 2, light 15 | No collision, invisible, light 15 | 8 glass around glowstone, x4 | Invisible block on a light block of level 15, broken by hitting its interaction | Implemented |
| `cherry_planks`, `cherry_log`, `cherry_leaves`, `cherry_sapling`, `woodSlab.cherry` | Cherry wood | | Patched vanilla wood types | cherry log to 4 planks | 26.3 cherry wood family | Vanilla |
| `marble`, `armorStand`, `cukube` | Lang entries | | | | | Unfinished |

### 11.2 Slabs (`slabs` / `double_slabs` `hu_1` / `ho_1`, glass `ht_1` / `hn_1`, wool `hv_1` `hw_1` / `hp_1` `hq_1`)

| Variant | Stats | Recipe | Datapack | Status |
|---|---|---|---|---|
| netherrack | hardness 2, resistance 10, rock | `###` netherrack, x6 | custom slab | Implemented |
| raw_stone | same | `#D#` stone, smooth stone slab, stone, x6 | 26.3 stone slab | Vanilla |
| reversed_planks | wood | `###` oak reversed planks, x6 | custom slab | Implemented |
| obsidian | rock | `###` obsidian, x6 | custom slab | Implemented |
| oak_log | wood | `###` oak logs, x6 | custom slab | Implemented |
| glowstone | glass | `###` glowstone, x6 | custom slab drawn lit (see 11.10) | Partial (no light around) |
| slate | rock | `###` slate blocks, x6 | custom slab | Implemented |
| glass (`glass_slab`) | hardness 0.3, glass | `XXX` glass, x3 | custom slab on a barrier, as the slopes (see 11.4) | Partial (full block collision) |
| wool x16 (`wool_slab`, `wool_slab_2`) | hardness 0.8, cloth | `###` wool of the color, x1 | 26.3 wool slabs (x6) | Vanilla |
| cherry (`woodSlab.cherry`) | | | 26.3 cherry slab | Vanilla |

Slabs in the datapack take the top or bottom half from where the player clicks, as vanilla does. Two custom slabs cannot merge into a double slab (each custom block is placed in its own space); the double model only shows when a vanilla slab of the host kind is added to it.

### 11.3 Stairs (`dc`, BlockStairs with the base block's stats)

| Id | Base | Recipe (x4 unless noted) | Datapack | Status |
|---|---|---|---|---|
| `raw_stone_stairs` | stone | none (the mod's stone recipe gives the vanilla cobblestone stairs) | 26.3 stone stairs | Vanilla |
| `log_stairs` | oak log | 6 oak logs | custom stairs | Implemented |
| `glowstone_stairs` | glowstone, light 15 | 6 glowstone | custom stairs drawn lit (see 11.10) | Partial (no light around) |
| `iron_stairs` | iron block | 6 iron ingots | custom stairs | Implemented |
| `obsidian_stairs` | obsidian | 6 obsidian ingots | custom stairs | Implemented |
| `glass_stairs` | glass | 6 glass | custom stairs on a barrier, as the slopes | Partial (see 11.4) |
| `step_stairs` | stone, smooth stone slab texture | 6 smooth stone slabs | custom stairs | Implemented |
| `slate_stairs` | stone, slate block texture | 6 slate items, x2 | custom stairs | Implemented |
| `oak_reversed_planks_stairs` | reversed oak planks | 6 reversed oak planks | custom stairs | Implemented |
| `<color>_wool_stairs` x16 | wool | 6 wool of the color | 26.3 wool stairs | Vanilla |
| `lapisLazulisStairs`, `redstoneStairs` | lang only | | | Unfinished |

### 11.4 Slopes (`dc` stairs blocks with the `slopes`, `inner_slopes`, `outer_slopes` models)

Collision is the stairs one in the original. A stairs host would show through the slope model, so the datapack puts slopes on a barrier with an interaction to break them: full block collision, straight shape only, facing taken from the player's look and the half from where the player clicks. Players next to a slope get 0.5 more step height, so they walk up it without jumping.

| Id | Texture | Recipe | Status |
|---|---|---|---|
| `stone_slopes` | stone | `__# / _#_ / ###` or mirrored, 6 stone, x4 | Partial (see above) |
| `slate_slopes` | slate block | 6 slate items, x2 | Partial |
| `sandstone_slopes` | sandstone | 6 sandstone, x2 | Partial |
| `glowstone_slopes` | glowstone, light 15 | 6 glowstone, x4 | Partial (drawn lit, no light around, see 11.10) |
| `glass_slopes` | glass | 6 glass, x2 | Partial |
| `oak_planks_slopes`, `spruce_`, `birch_`, `jungle_planks_slopes` | planks | 6 planks, x4 (oak) or x2 | Partial |
| `oak_log_slopes`, `spruce_`, `birch_`, `jungle_log_slopes` | log | 6 logs, x4 (oak) or x2 | Partial |
| `cornerWood`, `cornerLog`, `cornerStone`, `cornerGlowStone` | lang only | | Unfinished |

### 11.5 Walls (`walls`, `hk_1`, cobblestone wall behaviour)

Recipe: `### / ###` of the material, x5.

| Meta | Variant | Material | Datapack | Status |
|---|---|---|---|---|
| 0 | oak_log | oak log | custom wall on a cobblestone wall, dropping even when mined by hand | Implemented |
| 1 | stonebrick | stone bricks | 26.3 stone brick wall | Vanilla |
| 2 | stone | stone | custom wall | Implemented |
| 3 | oak_plank | sticks (that is the recipe of the jar) | custom wall | Implemented |
| 4 | brick | bricks | 26.3 brick wall | Vanilla |
| 5 | sandstone | sandstone | 26.3 sandstone wall | Vanilla |
| 6 | glowstone | glowstone | custom wall drawn lit (see 11.10) | Partial (no light around) |
| 7 | slate | slate block | custom wall | Implemented |
| | `wall.cobblestone` lang entry | | 26.3 cobblestone wall | Vanilla |

### 11.6 Fences and gates (`ar` fences, `as` gates, `go_1` colored iron fence)

| Id | Stats | Recipe | Datapack | Status |
|---|---|---|---|---|
| `glowstone_fence` | hardness 0.3, glass, light 15 | `X#X / X#X` sticks and glowstone, x6 | custom fence drawn lit (see 11.10) | Partial (no light around) |
| `log_fence` | hardness 2, wood | sticks and oak logs, x2 | custom fence | Implemented |
| `stone_fence` | hardness 1.5, resistance 10 | sticks and stone, x2 | custom fence | Implemented |
| `iron_fence` x16 (`go_1`) | hardness 5, resistance 10, metal, tinted by color | sticks and iron ingots, x2 (white), then 8 fences around a dye, x8 (the jar skips black through an index slip, the datapack does not) | 16 tinted custom fences on the nether brick fence | Implemented |
| `glowstone_fence_gate` | light 15 | `#W# / #W#` stone sticks and glowstone, x2 | custom gate drawn lit (see 11.10) | Partial (no light around) |
| `log_fence_gate` | wood | stone sticks and oak logs, x2 | custom gate | Implemented |
| `stone_fence_gate` | rock | stone sticks and stone, x2 | custom gate | Implemented |
| `iron_fence_gate` | metal | stone sticks and iron ingots, x2 | custom gate | Implemented |
| `woolFence` x16, `logFence.wood` | English lang only | | | Unfinished |

### 11.7 Trapdoors, pressure plate, ladder

| Id | Stats | Recipe | Datapack | Status |
|---|---|---|---|---|
| `stone_trapdoor` (`dx`) | hardness 3, rock | `#XX` stone stick and 2 stone, x4 | custom trapdoor on the oak trapdoor, opened by hand like the original | Implemented (wood sounds) |
| `glowstone_trapdoor` | hardness 0.3, light 15 | `#XX` stone stick and 2 glowstone, x4 | custom trapdoor on the oak trapdoor, drawn lit (see 11.10) | Partial (no light around) |
| `glowstone_pressure_plate` (`bn_0`, MOBS sensitivity) | hardness 0.3, light 15 | `##` glowstone, x3 | custom plate on the stone pressure plate (mobs and players), drawn lit (see 11.10) | Partial (no light around) |
| `iron_ladder` (`au_0`, the vanilla ladder class) | hardness 2.5, resistance 8, metal | `# # / ### / # #` iron ingots, x6 | custom ladder on the vanilla ladder: climbable, attaches to the wall the player looks at | Implemented |

### 11.8 Wool slabs and stairs

See 11.2 and 11.3: 16 colors each, vanilla wool textures (`wool_colored_<color>` in 1.8). 26.3 has its own wool slabs and stairs in the 16 colors, so the datapack has none.

### 11.9 Light blocks

| Id | Stats | Behaviour | Recipe | Datapack | Status |
|---|---|---|---|---|---|
| `lantern` oak, spruce, birch, jungle (`gu_1`) | hardness 1.5, wood, light 15 | Log with a glowing window (`cube_bottom_top`) | 8 logs around glowstone, x4 | 4 blocks on ochre froglight | Implemented |
| `lantern` iron | same | Iron block with a lamp | 8 iron ingots around glowstone, x4 | block on ochre froglight | Implemented |
| `red_light_off` / `red_light_on` (`ha_1`) | hardness 4.5, resistance 10, light 15 when on | Red redstone lamp | 8 redstone around a redstone lamp | block on the vanilla redstone lamp, its model follows the lit state | Implemented |
| `redstone_lamp_always` | hardness 0.3, glass, light 15 | Always lit redstone lamp, no creative tab | none | block on ochre froglight with the lit lamp texture | Implemented |
| `lamp_off` / `lamp_on` x16 (`gt_1`) | hardness 2, resistance 5, wood, light 15 when on | Hanging or standing lantern tinted by color, connects to rods, lamps and solid blocks (6 directions), lit with flint and steel, a lit lamp drops an unlit one | `XXX / WYW / XXX` rods, torch, glass, x4; colors with 8 lamps and a dye | `<color>_lamp` on a structure void and `<color>_lit_lamp` on a light block of level 15, tinted, connecting, lit by using flint and steel on them | Implemented |
| `rod` x16 (`hb_1`) | hardness 2, resistance 5, wood | Thin tinted rod connecting like the lamps | 2 sticks vertical, x2; colors with a dye | 16 rods on a structure void, without collision | Implemented |
| `lignite_torch` (`du`, torch class) | light 15 | Torch with a lignite tip | lignite over a steel stick, x4 | block on the vanilla torch, or on the vanilla wall torch when placed against the side of a block (`lignite_wall_torch`, dropping the lignite torch) | Implemented (light 14 of the vanilla torch) |

### 11.10 Light emission of glowstone shapes

Glowstone stairs, slabs, slopes, walls, fences, gates, trapdoor and pressure plate emit light 15 in the mod. No vanilla stairs, slab, wall, fence, gate, trapdoor or plate emits light, and the only invisible host giving light, the light block, has no collision. So these blocks keep the collision of their shape and their models are drawn at full light (`light_emission` 15 on every element): they look lit at night, but they light nothing around them. Lamps without collision (transparent light block, lit lamps) stand on a light block of level 15 and do light their surroundings.

### 11.11 How custom shaped blocks work in the datapack

Every block of sections 11 to 13 is a vanilla host block plus an item display (`user/original`). The display shows the original 1.8 models, converted to 26.3 at build time from `assets/original` (`blocks/` to `block/`, renamed vanilla textures, the vanilla 1.8 parents copied next to them). A decision tree generated from the original blockstate file picks the model and rotation for the host state (stairs shape, slab type, fence and wall sides, gate, trapdoor, plate, ladder, lamp, furnace, brewing stand and cake states) or for the neighbours (tables, benches, lamps, rods); it runs on placement and once per second. Blocks the original made invisible or without collision stand on a structure void, a light block or a barrier, with an interaction entity to break them by hitting it; flowers and flatware stand on a tripwire, whose string drop turns into the block. Each element of the converted models grows by 1/16 of a pixel on every side, so a face lying on a face of the host block is always drawn in front of it (a scaling of the whole display left thin parts such as fence rails nearly on the host and fighting with it). A display entity turns a model with its textures, so a blockstate rotation with `uvlock` is baked into a turned copy of the model whose faces map their texture from the world grid. Slabs, stairs, slopes and trapdoors take their half from where the player clicks, found by stepping along the player's look through the placed block.

## 12. Furniture (materials oak, birch, cobblestone, stone, enum `gy_1`)

All furniture: hardness 2, resistance 5, decoration tab. Recipe material: oak planks, birch planks, cobblestone, and stone meta 1 for stone (granite in 1.8, read as stone in the datapack).

| Id | Bounds | Behaviour | Recipe | Datapack | Status |
|---|---|---|---|---|---|
| `table` | full block | Legs disappear where tables touch (`table`, `_e`, `_es`, `_empty` models) | `XXX / # # / # #` material and sticks | 4 tables, connecting to tables | Implemented |
| `little_table` | 16 x 7.2 x 16 | Same models; the jar connects them to tables only | `XXX / # #` | 4 little tables, connecting to little tables | Implemented |
| `stool` (`he_1`) | 0.19-0.81, 0.6 high | Right click to sit (y + 0.05) | `XX / ##` material over sticks | 4 stools, sitting | Implemented |
| `high_stool` (`gq_1`) | 0.87 high | Right click to sit (y + 0.35) | `XX / ## / ##` | 4 high stools, sitting | Implemented |
| `bench` (`ga_1`) | | Connects to benches (`_n`, `_ne`, `_ns`, `_nse`, `_nsew`), single bench uses the stool model, sitting | `### / XXX` material over sticks | 4 benches, connecting, sitting | Implemented |
| `chair` (`gh_1`) | seat plus back, facing | Right click to sit (y - 0.05) | `__# / ### / X X` | 4 chairs facing the player, sitting | Implemented |
| `oak_shelf` (`hc_1`) | 0.69 deep, facing | Decorative shelf | `XXX / X X / X X` planks, x2 | custom shelf model facing the player | Implemented |
| `barrel` (`gz_1`) | | Chest-like container "Tonneau" | `XXX / ### / XXX` oak planks and iron ingots, x4 | block on the vanilla barrel (27 slots) with the IYC model | Implemented |
| `flatware` (`gp_1`) | 0.07 high plate | Cutlery to put on tables | `X#X / X#X` iron ingots and glass, x2 | flat model on a light-less structure void, broken by hitting it | Implemented |

Furniture (tables, little tables, seats, shelf) sits on a barrier and an interaction entity: three hits on the interaction, each less than a second after the previous one, break the block (the original took hardness 2 of mining), with particles of the block and the sound of its material, right clicking a seat mounts an invisible seat entity at the seat height, sneaking stands up. The interaction of tables stops under the top so blocks can still be placed on them. Every piece has a full block collision.

## 13. Special blocks

| Id | Stats | Original behaviour | Recipe | Datapack | Status |
|---|---|---|---|---|---|
| `jumpbox` (`gs_1`) | hardness 2.5, resistance 5, wood | Collision box 1/8 lower, any living entity standing in it gets +4.0 vertical motion, fall distance reset, piston sound | none in the mod (the datapack keeps its oak planks + ruby recipe) | `box_jump` on oak planks: players get 4 ticks of levitation 127 (about 60 blocks up, the original reached about 63) and 72 more safe fall distance until they land, mobs get an upward motion of 4.0 | Implemented (full block collision) |
| `speedBox` | lang and texture only | | | `box_speed`, speed effect when standing on it | Unfinished (datapack Extra) |
| `bombe` (`gd_1`, entity `he_2`) | hardness 0 | TNT that primes like TNT, fuse 120 ticks (random 15 to 45 when set off by another explosion), large smoke particles, explosion power 12 (TNT 4) | 9 TNT | `nuclear_bomb` on vanilla TNT: once lit, its primed TNT gets fuse 120 (15 to 44 when set off by an explosion) and `explosion_power` 12 | Implemented (the primed bomb looks like TNT) |
| `fire_camp` cobblestone, stone, brick, stonebrick, sandstone (`gf_1`) | hardness 1.5, resistance 10, light 15, 9/16 high | Burns entities inside (fire damage 1), flame and smoke particles, fire sound | the block + flint and steel, shapeless, x4 | 5 campfires on the vanilla campfire, whose flames, smoke, sound, light and burn damage show above the original stone ring; the charcoal it drops becomes the campfire | Implemented |
| `effect_generator` x8 (`gm_1`) | hardness 1.5, resistance 10 | Particles above the block on random display ticks: black smoke (10 smoke), portal, explosion (large explode), white smoke (10 explode), lava, water (10 splash), big black smoke (10 large smoke in the block volume), heart | none (creative) | 8 blocks on cobblestone with the piston texture, particles once per second | Implemented |
| `cloud` x16 (`gj_1`) | hardness 0.8, cloth, translucent, tinted | No collision, entities inside have their fall distance reset | 8 white wool around a water bucket, x8; colors: 8 clouds around a dye, x8 | 16 tinted clouds on a structure void with an interaction to break them; mobs inside lose their fall distance, players get 1 s of slow falling since theirs cannot be written | Implemented |
| `blob` x16 (`hi_1`) | hardness 0.5, resistance 2, translucent, tinted | Translucent colored block, creative tab only for staff accounts | 8 blobs around a dye | 16 translucent tinted blobs on a barrier, broken by hitting their interaction; the white one only from the creative menu, as the mod's staff only tab | Implemented |
| `sand_colored` x16 (`ap`) | sand stats, tinted | Falling sand in 16 colors | 8 sand around a dye, x8 | 26.3 concrete powder, which the original recipe now crafts | Vanilla |
| `blue_block_CTF`, `red_block_CTF` (`ge_1`) | resistance 6000000, unbreakable | Capture the flag walls: solid or passable depending on the player's team and the server game state | none (the datapack crafts 8 from wool around glass) | Two decorative blocks on glass | Partial (team logic is a server feature) |
| `iron_furnace` / `lit_iron_furnace` (`gr_1`, tile `ic_2`) | hardness 3.5, light 15 when lit | Furnace cooking in 100 ticks instead of 200 | 8 iron ingots around a furnace | block on the vanilla furnace, its model following the lit state, cooking progress pushed one more tick each tick while lit (the 26.3 `speed_multiplier` of the furnace resets when it lights up) | Implemented |
| `steel_brewing_stand` (`hd_1`, tile `ie_2`, item `steel_brewing_stand_item`) | hardness 0.8, light 0.3 | Brewing stand brewing in 250 ticks instead of 400 | `_B_ / ###` blaze rod over 3 steel blocks | block on the vanilla brewing stand with the steel models of each bottle state, `BrewTime` lowered one more tick 60 percent of the ticks (about 250 ticks, measured 1.56 units per tick) | Implemented |
| `cherry_cake` (`gi_1`) | hardness 0.5, cloth | Cake with cherry textures | cherry over cake | block on the vanilla cake, model follows the bites | Implemented |
| `blue_flower` (`gc_1`) | | Touching it poisons for 5 s (7.5 s normal, 15 s hard) | | flower on a tripwire, poison for 5, 8 or 15 s to players and mobs | Implemented |
| `white_flower` (`hm_1`) | | Touching it gives slowness for the same durations | | flower on a tripwire, slowness on touch to players and mobs | Implemented |
| `black_flower` (`gb_1`) | | Touching it deals 1 cactus damage | | flower on a tripwire, cactus damage on touch to players and mobs | Implemented |
| `hidden_door` | | | | | Unfinished |
| `hologram.*`, `laser.*`, `spot_*` | English lang only | | | | Unfinished |

## 14. Entities

| Entity | Original | Datapack | Status |
|---|---|---|---|
| `PrimedBombe` (`he_2`) | Primed bomb, see 13 | vanilla primed TNT with fuse and power set | Implemented |
| `crossbowarrow` (`hd_2`) | Bolt, damage 3.0, death message "s'est fait tirer dessus par" | vanilla arrow, damage x1.5 from the crossbow's enchantment | Implemented (vanilla death message) |
| Painting `Tele` (`zl_0.B`, 48 x 32 in `iyc:textures/painting/paintings.png`) | Extra painting variant drawn from the IYC texture | `tele` custom painting 3 x 2 | Implemented |

## 15. Gameplay tweaks (vanilla recipes added by the mod, end of `iu_1`)

| Result | Recipe | Datapack | Status |
|---|---|---|---|
| flint | 1 gravel | shapeless recipe | Implemented |
| ender pearl | 4 slime balls (2x2) | shaped recipe | Implemented |
| saddle x2 | `### / XXX` leather and iron ingots | shaped recipe | Implemented |
| slime ball x8 | 8 lime dye around a diamond | shaped recipe | Implemented |
| ice x4 | water bucket over a snow block | shaped recipe | Implemented |
| snow block | 2 snowballs side by side | shaped recipe (vanilla needs 4) | Implemented |
| cobweb x4 | 9 string | shaped recipe | Implemented |
| grass block x4 | water bucket, hops seeds, dirt (vertical) | shaped recipe | Implemented |
| vine x8 | 8 leaves around an ender pearl | shaped recipe | Implemented |
| chiseled stone bricks x4 | 8 stone bricks in a ring | shaped recipe | Implemented |
| cracked stone bricks x4 | 8 stone bricks around gunpowder | shaped recipe | Implemented |
| mossy stone bricks x4 | 8 vines around a stone brick | shaped recipe | Implemented |
| mossy cobblestone x4 | 8 vines around cobblestone | shaped recipe | Implemented |
| sponge x4 | `X#X / #W# / X#X` wool, string, yellow dye | shaped recipe | Implemented |
| red / brown mushroom block x4 | `#X# / XVX / #X#` mushrooms, bone meal, wool | shaped recipes | Implemented |
| cherry planks x4 | cherry log | | Vanilla |
| cobblestone stairs x4 | 6 stone (1.8 `stone_stairs` is cobblestone) | | Vanilla (26.3 crafts stone stairs from stone) |
| 4 light blocks | 8 glass around glowstone (transparent light block) | shaped recipe | Implemented |
| 8 concrete powder | 8 sand around a dye (colored sand) | 16 shaped recipes | Implemented |

## 16. Resource pack tweaks (`assets/minecraft` of the jar)

| Tweak | Original | Status |
|---|---|---|
| Connected glass | MCPatcher CTM for glass, the 16 stained glass and their panes (`mcpatcher/ctm/default/*`) | Out of scope (needs OptiFine or Continuity, a vanilla resource pack cannot connect textures) |
| Connected bookshelf | CTM horizontal method on bookshelves | Out of scope (same) |
| Sandstone top | CTM `top` method on sandstone sides | Out of scope (same) |
| OptiFine natural textures template | `optifine/template.natural.properties`, inactive template | Out of scope |
| Shaders | `shaders/post` and `shaders/program` are the vanilla 1.8 super secret settings | Vanilla |
| Font | `font/glyph_sizes.bin`, vanilla | Vanilla |
| Splash texts | `iyc/texts/splashes.txt`, 37 IYC splashes ("Bon jeu sur IYC", "Pense a voter", "Semi-RP"...) | Out of scope (26.3 reads splashes from `minecraft:texts/splashes.txt` only, which would replace the vanilla ones) |
| Title panoramas | `iyc/textures/gui/title/background/0..2` (day, evening, night) from the launcher assets | Out of scope (client menu) |
| GUI textures | `iyc/textures/gui/IYC.png`, `jobs.png`, `logo.png`, `widgets.png` | Out of scope (client GUI) |
| Sounds | `mariosound`, `scream`, `stop`, `monstercat`, `nyancat` in the asset index | Partial (the datapack ships `Ahhhhhrrr`, `Block Party Thing`, `Nyan Cat` sound events) |

## 17. Client and server features

| Feature | Original | Status |
|---|---|---|
| IYC interface (key `key.interface`) | Spawn, home, set home, wiki (Codex), site, jobs, pay, shop code send and check buttons, money, rank, town, faction, level display | Out of scope (server plugin and client GUI) |
| Jobs | mineur, pecheur, bucheron, netherien, verrier, fermier, forgeron, alchimiste, mercenaire, braconnier, cuisinier, leave job with a cost warning | Out of scope (server economy) |
| Armor and effects HUD toggles | `key.armorInGame`, `key.effectInGame` | Out of scope (client HUD) |
| Options | join / left messages, vote messages, durability display | Out of scope (client options) |
| Staff only creative items | `fu_2.hX` and a username whitelist for blob and some wands | Out of scope (account checks) |
| Capture the flag game state | `fs_2` team and game flags read by the CTF blocks | Out of scope (server minigame) |
| Web radios | `record_your_radio`, `record_thelan` | Out of scope |
| Cosmetics | helice hat, reindeer antlers drawn on granted players | Out of scope (see Extra helice hat) |

## 18. Datapack additions not in the mod

| Item | Behaviour | Status |
|---|---|---|
| Obsidian and steel tools and armor | own tiers | Extra |
| `helice_hat` | lowers gravity on the head | Extra |
| `quiver`, `old_ruby`, `blank` | items without behaviour | Extra |
| `rock` | throwable snowball dealing 2 damage, 5 percent from cobblestone drops | Extra (author notes) |
| `box_speed` | speed effect when standing on it, from the unregistered `speedBox` texture | Extra |
| Taurine, cola and caffeine drops | from sugar cane, wheat and hops items | Extra (author notes) |
| Lignite as fuel | burns longer than coal | Extra (author notes) |
| Deepslate ore variants | 26.3 depth | Extra |

