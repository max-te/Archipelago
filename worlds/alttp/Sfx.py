from dataclasses import dataclass, field
from random import Random
from typing import Optional

"""
    This file is a port of https://github.com/sporchia/alttp_vt_randomizer/blob/70e5be4e3a0e88090bfe730f8500130b591000ca/resources/js/sfx.js
"""


@dataclass
class Sfx:
    name: str
    sfx_set: int
    orig_id: int
    addr: int
    chain: list[int] = field(default_factory=list)
    accomp: bool = False

    target_set: Optional[int] = None
    target_id: Optional[int] = None
    target_chain: Optional[int] = None

def make_sound_table():
    return [
      Sfx("Slash1", 0x02, 0x01, 0x2614, []),
      Sfx("Slash2", 0x02, 0x02, 0x2625, []),
      Sfx("Slash3", 0x02, 0x03, 0x2634, []),
      Sfx("Slash4", 0x02, 0x04, 0x2643, []),
      Sfx("Wall clink", 0x02, 0x05, 0x25dd, []),
      Sfx("Bombable door clink", 0x02, 0x06, 0x25d7, []),
      Sfx("Fwoosh shooting", 0x02, 0x07, 0x25b7, []),
      Sfx("Arrow hitting wall", 0x02, 0x08, 0x25e3, []),
      Sfx("Boomerang whooshing", 0x02, 0x09, 0x25ad, []),
      Sfx("Hookshot", 0x02, 0x0a, 0x25c7, []),
      Sfx("Placing bomb", 0x02, 0x0b, 0x2478, []),
      Sfx("Bomb exploding/Quake/Bombos/Exploding wall",0x02,0x0c,0x269c,[]),
      Sfx("Powder", 0x02, 0x0d, 0x2414, [0x3f]),
      Sfx("Fire rod shot", 0x02, 0x0e, 0x2404, []),
      Sfx("Ice rod shot", 0x02, 0x0f, 0x24c3, []),
      Sfx("Hammer use", 0x02, 0x10, 0x23fa, []),
      Sfx("Hammering peg", 0x02, 0x11, 0x23f0, []),
      Sfx("Digging", 0x02, 0x12, 0x23cd, []),
      Sfx("Flute use", 0x02, 0x13, 0x23a0, [0x3e]),
      Sfx("Cape on", 0x02, 0x14, 0x2380, []),
      Sfx("Cape off/Wallmaster grab", 0x02, 0x15, 0x2390, []),
      Sfx("Staircase", 0x02, 0x16, 0x232c, []),
      Sfx("Staircase", 0x02, 0x17, 0x2344, []),
      Sfx("Staircase", 0x02, 0x18, 0x2356, []),
      Sfx("Staircase", 0x02, 0x19, 0x236e, []),
      Sfx("Tall grass/Hammer hitting bush", 0x02, 0x1a, 0x2316, []),
      Sfx("Mire shallow water", 0x02, 0x1b, 0x2307, []),
      Sfx("Shallow water", 0x02, 0x1c, 0x2301, []),
      Sfx("Lifting object", 0x02, 0x1d, 0x22bb, []),
      Sfx("Cutting grass", 0x02, 0x1e, 0x2577, []),
      Sfx("Item breaking", 0x02, 0x1f, 0x22e9, []),
      Sfx("Item falling in pit", 0x02, 0x20, 0x22da, []),
      Sfx("Bomb hitting ground/General bang", 0x02, 0x21, 0x22cf, []),
      Sfx("Pushing object/Armos bounce", 0x02, 0x22, 0x2107, []),
      Sfx("Boots dust", 0x02, 0x23, 0x22b1, []),
      Sfx("Splashing", 0x02, 0x24, 0x22a5, [0x3d]),
      Sfx("Mire shallow water again?", 0x02, 0x25, 0x2296, []),
      Sfx("Link taking damage", 0x02, 0x26, 0x2844, []),
      Sfx("Fainting", 0x02, 0x27, 0x2252, []),
      Sfx("Item splash", 0x02, 0x28, 0x2287, []),
      Sfx("Rupee refill", 0x02, 0x29, 0x243f, [0x3b]),
      Sfx( "Fire rod shot hitting wall/Bombos spell", 0x02, 0x2a, 0x2033, []),
      Sfx("Heart beep/Text box", 0x02, 0x2b, 0x1ff2, []),
      Sfx("Sword up", 0x02, 0x2c, 0x1fd9, [0x3a]),
      Sfx("Magic drain", 0x02, 0x2d, 0x20a6, []),
      Sfx("GT opening", 0x02, 0x2e, 0x1fca, [0x39]),
      Sfx("GT opening/Water drain", 0x02, 0x2f, 0x1f47, [0x38]),
      Sfx("Cucco", 0x02, 0x30, 0x1ef1, []),
      Sfx("Fairy", 0x02, 0x31, 0x20ce, []),
      Sfx("Bug net", 0x02, 0x32, 0x1d47, []),
      Sfx("Teleport2", 0x02, 0x33, 0x1cdc, [], True),
      Sfx("Teleport1", 0x02, 0x34, 0x1f6f, [0x33]),
      Sfx("Quake/Vitreous/Zora king/Armos/Pyramid/Lanmo", 0x02, 0x35, 0x1c67, [0x36]),
      Sfx( "Mire entrance (extends above)", 0x02, 0x36, 0x1c64, [], True),
      Sfx("Spin charged", 0x02, 0x37, 0x1a43, []),
      Sfx("Water sound", 0x02, 0x38, 0x1f6f, [], True),
      Sfx("GT opening thunder", 0x02, 0x39, 0x1f9c, [], True),
      Sfx("Sword up", 0x02, 0x3a, 0x1fe7, [], True),
      Sfx("Quiet rupees", 0x02, 0x3b, 0x2462, [], True),
      Sfx("Error beep", 0x02, 0x3c, 0x1a37, []),
      Sfx("Big splash", 0x02, 0x3d, 0x22ab, [], True),
      Sfx("Flute again", 0x02, 0x3e, 0x23b5, [], True),
      Sfx("Powder paired", 0x02, 0x3f, 0x2435, [], True),

      Sfx("Sword beam", 0x03, 0x01, 0x1a18, []),
      Sfx("TR opening", 0x03, 0x02, 0x254e, []),
      Sfx("Pyramid hole", 0x03, 0x03, 0x224a, []),
      Sfx("Angry soldier", 0x03, 0x04, 0x220e, []),
      Sfx("Lynel shot/Javelin toss", 0x03, 0x05, 0x25b7, []),
      Sfx( "BNC swing/Phantom ganon/Helma tail/Arrghus swoosh", 0x03, 0x06, 0x21f5, []),
      Sfx("Cannon fire", 0x03, 0x07, 0x223d, []),
      Sfx("Damage to enemy; $0BEX.4=1", 0x03, 0x08, 0x21e6, []),
      Sfx("Enemy death", 0x03, 0x09, 0x21c1, []),
      Sfx("Collecting rupee", 0x03, 0x0a, 0x21a9, []),
      Sfx("Collecting heart", 0x03, 0x0b, 0x2198, []),
      Sfx("Non-blank text character", 0x03, 0x0c, 0x218e, []),
      Sfx( "HUD heart (used explicitly by sanc heart?)", 0x03, 0x0d, 0x21b5, []),
      Sfx("Opening chest", 0x03, 0x0e, 0x2182, []),
      Sfx("♪Do do do doooooo♫", 0x03, 0x0f, 0x24b9, [ 0x3c, 0x3d, 0x3e, 0x3f,]),
      Sfx("Opening/Closing map (paired)", 0x03, 0x10, 0x216d, [ 0x3b,]),
      Sfx( "Opening item menu/Bomb shop guy breathing", 0x03, 0x11, 0x214f, []),
      Sfx( "Closing item menu/Bomb shop guy breathing", 0x03, 0x12, 0x215e, []),
      Sfx( "Throwing object (sprites use it as well)/Stalfos jump", 0x03, 0x13, 0x213b, []),
      Sfx( "Key door/Trinecks/Dash key landing/Stalfos Knight collapse", 0x03, 0x14, 0x246c, []),
      Sfx( "Door closing/OW door opening/Chest opening (w/ $29 in $012E)", 0x03, 0x15, 0x212f, []),
      Sfx("Armos Knight thud", 0x03, 0x16, 0x2123, []),
      Sfx("Rat squeak", 0x03, 0x17, 0x25a6, []),
      Sfx("Dragging/Mantle moving", 0x03, 0x18, 0x20dd, []),
      Sfx( "Fireball/Laser shot; Somehow used by Trinexx???", 0x03, 0x19, 0x250a, []),
      Sfx("Chest reveal jingle ", 0x03, 0x1a, 0x1e8a, [0x38]),
      Sfx("Puzzle jingle", 0x03, 0x1b, 0x20b6, [0x3a]),
      Sfx("Damage to enemy", 0x03, 0x1c, 0x1a62, []),
      Sfx("Potion refill/Magic drain", 0x03, 0x1d, 0x20a6, []),
      Sfx( "Flapping (Duck/Cucco swarm/Ganon bats/Keese/Raven/Vulture)", 0x03, 0x1e, 0x2091, []),
      Sfx("Link falling", 0x03, 0x1f, 0x204b, []),
      Sfx("Menu/Text cursor moved", 0x03, 0x20, 0x276c, []),
      Sfx("Damage to boss", 0x03, 0x21, 0x27e2, []),
      Sfx("Boss dying/Deleting file", 0x03, 0x22, 0x26cf, []),
      Sfx("Spin attack/Medallion swoosh", 0x03, 0x23, 0x2001, [ 0x39,]),
      Sfx("OW map perspective change", 0x03, 0x24, 0x2043, []),
      Sfx("Pressure switch", 0x03, 0x25, 0x1e9d, []),
      Sfx( "Lightning/Game over/Laser/Ganon bat/Trinexx lunge", 0x03, 0x26, 0x1e7b, []),
      Sfx("Agahnim charge", 0x03, 0x27, 0x1e40, []),
      Sfx("Agahnim/Ganon teleport", 0x03, 0x28, 0x26f7, []),
      Sfx("Agahnim shot", 0x03, 0x29, 0x1e21, []),
      Sfx( "Somaria/Byrna/Ether spell/Helma fire ball", 0x03, 0x2a, 0x1e12, []),
      Sfx("Electrocution", 0x03, 0x2b, 0x1df3, []),
      Sfx("Bees", 0x03, 0x2c, 0x1dc0, []),
      Sfx("Milestone, also via text", 0x03, 0x2d, 0x1da9, [0x37]),
      Sfx("Collecting heart container", 0x03, 0x2e, 0x1d5d, [ 0x35, 0x34,]),
      Sfx("Collecting absorbable key", 0x03, 0x2f, 0x1d80, [0x33]),
      Sfx( "Byrna spark/Item plop/Magic bat zap/Blob emerge", 0x03, 0x30, 0x1b53, []),
      Sfx("Sprite falling/Moldorm shuffle", 0x03, 0x31, 0x1aca, []),
      Sfx( "Bumper boing/Somaria punt/Blob transmutation/Sprite boings", 0x03, 0x32, 0x1a78, []),
      Sfx("Jingle (paired $2F→$33)", 0x03, 0x33, 0x1d93, [], True),
      Sfx( "Depressing jingle (paired $2E→$35→$34)", 0x03, 0x34, 0x1d66, [], True),
      Sfx( "Ugly jingle (paired $2E→$35→$34)", 0x03, 0x35, 0x1d73, [], True),
      Sfx( "Wizzrobe shot/Helma fireball split/Mothula beam/Blue balls", 0x03, 0x36, 0x1aa7, []),
      Sfx( "Dinky jingle (paired $2D→$37)", 0x03, 0x37, 0x1db4, [], True),
      Sfx( "Apathetic jingle (paired $1A→$38)", 0x03, 0x38, 0x1e93, [], True),
      Sfx( "Quiet swish (paired $23→$39)", 0x03, 0x39, 0x2017, [], True),
      Sfx( "Defective jingle (paired $1B→$3A)", 0x03, 0x3a, 0x20c0, [], True),
      Sfx( "Petulant jingle (paired $10→$3B)", 0x03, 0x3b, 0x2176, [], True),
      Sfx( "Triumphant jingle (paired $0F→$3C→$3D→$3E→$3F)", 0x03, 0x3c, 0x248a, [], True),
      Sfx( "Less triumphant jingle ($0F→$3C→$3D→$3E→$3F)", 0x03, 0x3d, 0x2494, [], True),
      Sfx( '"You tried, I guess" jingle (paired $0F→$3C→$3D→$3E→$3F)', 0x03, 0x3e, 0x249e, [], True),
      Sfx( '"You didn\'t really try" jingle (paired $0F→$3C→$3D→$3E→$3F)', 0x03, 0x3f, 0x2480, [], True),
    ]

@dataclass
class SfxCandidate:
    set: int
    id: int

def shuffle_sfx_data(local_random: Random):
    sfx_map: dict[int, dict[int, Sfx]] = { 2: {}, 3: {} }
    accompaniment_map: dict[int, list[int]] = { 2: [], 3: [] }
    candidates: list[SfxCandidate] = []
    sfx_pool = make_sound_table()

    for sfx in sfx_pool:
        sfx_map[sfx.sfx_set][sfx.orig_id] = sfx
        if not sfx.accomp:
            candidates.append(SfxCandidate(sfx.sfx_set, sfx.orig_id))
        else:
            accompaniment_map[sfx.sfx_set].append(sfx.orig_id)
    
    chained_sfx = [sfx for sfx in sfx_pool if sfx.chain]

    local_random.shuffle(candidates)
    local_random.shuffle(chained_sfx)

    chained_sfx.sort(key=lambda sfx: len(sfx.chain), reverse=True)
    for chained in chained_sfx:
        chosen_slot = next((x for x in candidates if len(accompaniment_map[x.set]) >= len(chained.chain)))
        chained.target_set = chosen_slot.set
        chained.target_id = chosen_slot.id
        chained.target_chain = []

        for downstream in chained.chain:
            next_slot = accompaniment_map[chosen_slot.set].pop()
            ds_acc = sfx_map[chained.sfx_set][downstream]
            ds_acc.target_set = chosen_slot.set
            ds_acc.target_id = next_slot
            chained.target_chain.append(next_slot)
        
        candidates.remove(chosen_slot)
        sfx_pool.remove(chained)

    unchained_sfx = [sfx for sfx in sfx_pool if not sfx.accomp]
    for sfx in unchained_sfx:
        chosen_slot = candidates.pop()
        sfx.target_set = chosen_slot.set
        sfx.target_id = chosen_slot.id
    
    return sfx_map

def sfx_shuffle(rom, local_random: Random):
    sfx_table = {
      2: 0x1a8c29,
      3: 0x1a8d25,
    }

    sfx_accompaniment_table = {
      2: 0x1a8ca7,
      3: 0x1a8da3,
    }

    sfx_map = shuffle_sfx_data(local_random)
    sfx_sets = [sfx_map[2], sfx_map[3]]
    for shuffled_sfx in sfx_sets:
        for id in shuffled_sfx:
            sfx = shuffled_sfx[id]
            base_adress = sfx_table[sfx.target_set]
            rom.write_int16(
                base_adress + sfx.target_id * 2 - 2,
                sfx.addr
            )
            ac_base = sfx_accompaniment_table[sfx.target_set]
            last = sfx.target_id
            if sfx.target_chain:
                for chained in sfx.target_chain:
                    rom.write_byte(ac_base + last - 1, chained)
                    last = chained
            rom.write_byte(ac_base + last - 1, 0)