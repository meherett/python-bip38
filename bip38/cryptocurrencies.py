#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Dict, Optional
)


class ICryptocurrency:

    NETWORKS: Dict[str, Dict[str, int]]
    ALPHABET: Optional[str] = None


class Adcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb0,
            "address_prefix": 0x17
        }
    }


class Anon(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x582
        }
    }


class Argoneum(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbf,
            "address_prefix": 0x32
        }
    }


class Artax(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x97,
            "address_prefix": 0x17
        }
    }


class Aryacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x97,
            "address_prefix": 0x17
        }
    }


class Asiacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x97,
            "address_prefix": 0x17
        }
    }


class Auroracoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x97,
            "address_prefix": 0x17
        }
    }


class Avian(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x3c
        }
    }


class Axe(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xcc,
            "address_prefix": 0x37
        }
    }


class Bata(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa4,
            "address_prefix": 0x19
        }
    }


class BeetleCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x99,
            "address_prefix": 0x1a
        }
    }


class BelaCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x99,
            "address_prefix": 0x19
        }
    }


class BitCloud(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x99,
            "address_prefix": 0x19
        }
    }


class Bitcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x0
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x6f
        },
        "regtest": {
            "wif_prefix": 0xef,
            "address_prefix": 0x6f
        }
    }
    ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


class BitcoinAtom(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x17
        }
    }


class BitcoinGold(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x26
        }
    }


class BitcoinGreen(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x2e,
            "address_prefix": 0x26
        }
    }


class BitcoinPlus(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x99,
            "address_prefix": 0x19
        }
    }


class BitcoinPrivate(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1325
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x1957
        }
    }


class BitcoinSV(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x0
        }
    }


class BitcoinZ(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1cb8
        }
    }


class Bitcore(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x3
        }
    }


class BitSend(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xcc,
            "address_prefix": 0x66
        }
    }


class Blackcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x99,
            "address_prefix": 0x19
        }
    }


class Blocknode(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x4b,
            "address_prefix": 0x19
        },
        "testnet": {
            "wif_prefix": 0x89,
            "address_prefix": 0x55
        }
    }


class BlockStamp(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x0
        }
    }


class Bolivarcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xd5,
            "address_prefix": 0x55
        }
    }


class BritCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x99,
            "address_prefix": 0x19
        }
    }


class CanadaeCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9c,
            "address_prefix": 0x1c
        }
    }


class Cannacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9c,
            "address_prefix": 0x1c
        }
    }


class Clams(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x85,
            "address_prefix": 0x89
        }
    }


class ClubCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x99,
            "address_prefix": 0x1c
        }
    }


class Compcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9c,
            "address_prefix": 0x1c
        }
    }


class CPUChain(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1c
        }
    }


class CranePay(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x7b,
            "address_prefix": 0x1c
        }
    }


class Crave(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x99,
            "address_prefix": 0x46
        }
    }


class Dash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xcc,
            "address_prefix": 0x4c
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x8c
        }
    }


class DeepOnion(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9f,
            "address_prefix": 0x1f
        }
    }


class Defcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9e,
            "address_prefix": 0x1e
        }
    }


class Denarius(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9e,
            "address_prefix": 0x1e
        }
    }


class Diamond(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xda,
            "address_prefix": 0x5a
        }
    }


class DigiByte(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1e
        }
    }


class Digitalcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9e,
            "address_prefix": 0x1e
        }
    }


class Divi(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xd4,
            "address_prefix": 0x1e
        },
        "testnet": {
            "wif_prefix": 0xd4,
            "address_prefix": 0x1e
        }
    }


class Dogecoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xf1,
            "address_prefix": 0x1e
        },
        "testnet": {
            "wif_prefix": 0xf1,
            "address_prefix": 0x71
        }
    }


class Ecoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xdc,
            "address_prefix": 0x5c
        }
    }


class EDRCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xdd,
            "address_prefix": 0x5d
        }
    }


class eGulden(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb0,
            "address_prefix": 0x30
        }
    }


class Einsteinium(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa1,
            "address_prefix": 0x21
        }
    }


class Elastos(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x21
        }
    }


class Energi(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x6a,
            "address_prefix": 0x21
        }
    }


class EuropeCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa8,
            "address_prefix": 0x21
        }
    }


class Evrmore(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x21
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x6f
        }
    }


class ExclusiveCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa1,
            "address_prefix": 0x21
        }
    }


class Feathercoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x8e,
            "address_prefix": 0xe
        }
    }


class Firo(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xd2,
            "address_prefix": 0x52
        }
    }


class Firstcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa3,
            "address_prefix": 0x23
        }
    }


class FIX(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x3c,
            "address_prefix": 0x23
        },
        "testnet": {
            "wif_prefix": 0xed,
            "address_prefix": 0x4c
        }
    }


class Flashcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc4,
            "address_prefix": 0x44
        }
    }


class Flux(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1cb8
        }
    }


class Foxdcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x23
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x5f
        }
    }


class FujiCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa4,
            "address_prefix": 0x24
        }
    }


class GameCredits(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa6,
            "address_prefix": 0x26
        }
    }


class GCRCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9a,
            "address_prefix": 0x26
        }
    }


class GoByte(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc6,
            "address_prefix": 0x26
        }
    }


class Gridcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbe,
            "address_prefix": 0x3e
        }
    }


class GroestlCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x24
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x6f
        }
    }


class Gulden(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x62,
            "address_prefix": 0x26
        }
    }


class Helleniccoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb0,
            "address_prefix": 0x30
        }
    }


class Hempcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa8,
            "address_prefix": 0x28
        }
    }


class Horizen(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x2089
        }
    }


class Hush(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1cb8
        }
    }


class InsaneCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x37,
            "address_prefix": 0x66
        }
    }


class InternetOfPeople(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x31,
            "address_prefix": 0x75
        }
    }


class IXCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x8a
        }
    }


class Jumbucks(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xab,
            "address_prefix": 0x2b
        }
    }


class Kobocoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xa3,
            "address_prefix": 0x23
        }
    }


class Komodo(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbc,
            "address_prefix": 0x3c
        }
    }


class Landcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb0,
            "address_prefix": 0x30
        }
    }


class LBRYCredits(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x1c,
            "address_prefix": 0x55
        }
    }


class Linx(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xcb,
            "address_prefix": 0x4b
        }
    }


class Litecoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb0,
            "address_prefix": 0x30
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x6f
        }
    }


class LitecoinCash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb0,
            "address_prefix": 0x1c
        }
    }


class LitecoinZ(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0xab3
        }
    }


class Lkrcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb0,
            "address_prefix": 0x30
        }
    }


class Lynx(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xad,
            "address_prefix": 0x2d
        }
    }


class Mazacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xe0,
            "address_prefix": 0x32
        }
    }


class Megacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb2,
            "address_prefix": 0x32
        }
    }


class Minexcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x4b
        }
    }


class Monacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb0,
            "address_prefix": 0x32
        }
    }


class Monk(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x37,
            "address_prefix": 0x33
        }
    }


class Myriadcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb2,
            "address_prefix": 0x32
        }
    }


class Namecoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x34
        }
    }


class Navcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x96,
            "address_prefix": 0x35
        }
    }


class Neblio(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb5,
            "address_prefix": 0x35
        }
    }


class Neoscoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb1,
            "address_prefix": 0x35
        }
    }


class Neurocoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb5,
            "address_prefix": 0x35
        }
    }


class NewYorkCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbc,
            "address_prefix": 0x3c
        }
    }


class NIX(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x26
        }
    }


class Novacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x88,
            "address_prefix": 0x8
        }
    }


class NuBits(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x96,
            "address_prefix": 0x19
        }
    }


class NuShares(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x95,
            "address_prefix": 0x3f
        }
    }


class OKCash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x3,
            "address_prefix": 0x37
        }
    }


class Omni(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x0
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x6f
        }
    }


class Onix(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xcb,
            "address_prefix": 0x4b
        }
    }


class Particl(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x6c,
            "address_prefix": 0x38
        }
    }


class Peercoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb7,
            "address_prefix": 0x37
        }
    }


class Pesobit(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb7,
            "address_prefix": 0x37
        }
    }


class Phore(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xd4,
            "address_prefix": 0x37
        }
    }


class Pinkcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x83,
            "address_prefix": 0x3
        }
    }


class Pivx(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xd4,
            "address_prefix": 0x1e
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x8b
        }
    }


class PoSWCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb7,
            "address_prefix": 0x37
        }
    }


class Potcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb7,
            "address_prefix": 0x37
        }
    }


class ProjectCoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x75,
            "address_prefix": 0x37
        }
    }


class Putincoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xb7,
            "address_prefix": 0x37
        }
    }


class Qtum(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x3a
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x78
        }
    }


class Rapids(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x2e,
            "address_prefix": 0x3d
        }
    }


class Ravencoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x3c
        },
        "testnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x6f
        }
    }


class Reddcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbd,
            "address_prefix": 0x3d
        }
    }


class Ripple(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x0
        }
    }
    ALPHABET = "rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz"


class Ritocoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x8b,
            "address_prefix": 0x19
        }
    }


class RSK(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x0
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x6f
        }
    }


class Rubycoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbc,
            "address_prefix": 0x3c
        }
    }


class Safecoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbd,
            "address_prefix": 0x3d
        }
    }


class Saluscoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbf,
            "address_prefix": 0x3f
        }
    }


class Scribe(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x6e,
            "address_prefix": 0x3c
        }
    }


class ShadowCash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbf,
            "address_prefix": 0x3f
        },
        "testnet": {
            "wif_prefix": 0xff,
            "address_prefix": 0x7f
        }
    }


class Slimcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x46,
            "address_prefix": 0x3f
        },
        "testnet": {
            "wif_prefix": 0x57,
            "address_prefix": 0x6f
        }
    }


class Smileycoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x5,
            "address_prefix": 0x19
        }
    }


class Solarcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x92,
            "address_prefix": 0x12
        }
    }


class Stash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xcc,
            "address_prefix": 0x4c
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x8c
        }
    }


class Stratis(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbf,
            "address_prefix": 0x3f
        },
        "testnet": {
            "wif_prefix": 0xbf,
            "address_prefix": 0x41
        }
    }


class Sugarchain(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x3f
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x42
        }
    }


class Syscoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x3f
        }
    }


class ThoughtAI(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x7b,
            "address_prefix": 0x7
        }
    }


class TOACoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc1,
            "address_prefix": 0x41
        }
    }


class TWINS(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x42,
            "address_prefix": 0x49
        },
        "testnet": {
            "wif_prefix": 0xed,
            "address_prefix": 0x4c
        }
    }


class UltimateSecureCash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xbf,
            "address_prefix": 0x44
        }
    }


class Unobtanium(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xe0,
            "address_prefix": 0x82
        }
    }


class Vcash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc7,
            "address_prefix": 0x47
        }
    }


class Verge(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x9e,
            "address_prefix": 0x1e
        }
    }


class Vertcoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x47
        }
    }


class Viacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc7,
            "address_prefix": 0x47
        },
        "testnet": {
            "wif_prefix": 0xff,
            "address_prefix": 0x7f
        }
    }


class Vivo(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc6,
            "address_prefix": 0x46
        }
    }


class Voxels(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc6,
            "address_prefix": 0x46
        }
    }


class VirtualCash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc7,
            "address_prefix": 0x47
        }
    }


class Wagerr(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc7,
            "address_prefix": 0x49
        }
    }


class Whitecoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc9,
            "address_prefix": 0x49
        }
    }


class Wincoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xc9,
            "address_prefix": 0x49
        }
    }


class XUEZ(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xd4,
            "address_prefix": 0x4b
        }
    }


class Ycash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1c28
        }
    }


class Zcash(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1cb8
        },
        "testnet": {
            "wif_prefix": 0xef,
            "address_prefix": 0x1d25
        }
    }


class ZClassic(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x1cb8
        }
    }


class Zetacoin(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0xe0,
            "address_prefix": 0x50
        }
    }


class ZooBC(ICryptocurrency):

    NETWORKS = {
        "mainnet": {
            "wif_prefix": 0x80,
            "address_prefix": 0x0
        }
    }
