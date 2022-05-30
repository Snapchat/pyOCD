# pyOCD debugger
# Copyright (c) 2022 Huada Semiconductor Corporation
# Copyright (c) 2022 Chris Reed
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ...coresight.coresight_target import CoreSightTarget
from ...core.memory_map import (FlashRegion, RamRegion, MemoryMap)
from ...debug.svd.loader import SVDFile


class DBGMCU:
    STCTL = 0xE0042020
    STCTL_VALUE = 0x3

    TRACECTL = 0xE0042024
    TRACECTL_VALUE = 0x0

FLASH_ALGO = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 
    0x4770ba40, 0x4770ba40, 0x4770bac0, 0x4770bac0, 0x0030ea4f, 0x00004770, 0x0030ea4f, 0x00004770,
    0x5001f24a, 0x8008490a, 0x7800480a, 0x0007f020, 0x39264908, 0x0026f881, 0x68004807, 0x00f0f020,
    0x60084905, 0x49032001, 0x70081d09, 0x00004770, 0x4005440e, 0x40054026, 0x40010408, 0x5101f24a,
    0x80114a16, 0x6a094916, 0x0170f021, 0x4a143110, 0xf2406211, 0x68094104, 0x0001f001, 0x4911b150,
    0x60114a11, 0x68094911, 0x01f0f021, 0x4a0f3140, 0xe0096011, 0x4a0c490e, 0x490c6011, 0xf0216809,
    0x315001f0, 0x60114a09, 0x4a052100, 0x7011322a, 0x4a032105, 0x1026f882, 0x00004770, 0x4005440e,
    0x40054000, 0x10102781, 0x4005410c, 0x40010408, 0x10101f81, 0x4603b570, 0xe003460c, 0x5b01f814,
    0x5b01f803, 0xf1a21e15, 0xd1f70201, 0xb510bd70, 0xf81ef000, 0xb510bd10, 0x46204604, 0xf854f000,
    0x0000bd10, 0xf000b500, 0x4808f9d5, 0xf4206800, 0x49067080, 0x20016008, 0x20006008, 0x1e406008,
    0x390c4902, 0xf0006008, 0xbd00f9c5, 0x4001040c, 0xf000b500, 0xf7fff9bf, 0x481aff73, 0xf0206800,
    0x1c400001, 0x60084917, 0x68004608, 0x0070f020, 0x60083050, 0x68004608, 0x7080f420, 0x7080f500,
    0xf2416008, 0x21002034, 0xe0016008, 0xf9a2f000, 0x1d00480c, 0xf4006800, 0x28007080, 0xf000d0f6,
    0x4808f999, 0xf0206800, 0x49060070, 0x46086008, 0xf0206800, 0x60080001, 0xff60f7ff, 0xf98af000,
    0xbd002000, 0x4001040c, 0x4604b530, 0x4540f649, 0xff36f7ff, 0xf97ef000, 0x6800481d, 0x0001f020,
    0x491b1c40, 0x46086008, 0xf0206800, 0x30400070, 0x46086008, 0xf4206800, 0xf5007080, 0x60087080,
    0xf968f000, 0x2000bf00, 0xf0006020, 0xe001f963, 0xf960f000, 0x1d00480e, 0xf4006800, 0xb9107080,
    0x1e051e68, 0xf000d1f4, 0x4809f955, 0xf0206800, 0x49070070, 0x46086008, 0xf0206800, 0x60080001,
    0xf948f000, 0xff1af7ff, 0xf944f000, 0xbd302000, 0x4001040c, 0x4811b500, 0x60084911, 0x60084811,
    0x300c480f, 0xf4206800, 0xf5007080, 0x490c7080, 0x6008310c, 0x5001f24a, 0x8008490b, 0x6a00480b,
    0x40e0f420, 0x40c0f500, 0x62084908, 0x4025f44f, 0x80084905, 0xf91ef000, 0x0000bd00, 0xffff0123,
    0x40010400, 0xffff3210, 0x4005440e, 0x40054000, 0x45f8e92d, 0x460c4680, 0xf04f4615, 0x900030ff,
    0x4740f649, 0x493d203f, 0xf0006008, 0x483bf903, 0x68003808, 0x0001f020, 0x49381c40, 0x60083908,
    0x68004608, 0x0070f020, 0x60083030, 0x68004608, 0x7080f420, 0x7080f500, 0x46466008, 0xf000bf00,
    0xf04ff8e9, 0xe0260a00, 0x4740f649, 0x60306828, 0x1d2d1d36, 0xf8def000, 0xf000e001, 0x4827f8db,
    0x68001f00, 0x0010f000, 0x1e78b910, 0xd1f41e07, 0x2001b917, 0x85f8e8bd, 0x1f004820, 0xf0006800,
    0xb118000f, 0xf8c6f000, 0xe7f32001, 0x491b2010, 0xf10a6008, 0xebba0a01, 0xd3d50f94, 0x0003f004,
    0xf004b138, 0x46290203, 0xf7ff4668, 0x9800fec3, 0xf000c601, 0x4811f8af, 0x68003808, 0x0070f020,
    0x3908490e, 0x46086008, 0xf0206800, 0x60080001, 0x4740f649, 0xf000e001, 0x4808f89d, 0x68001f00,
    0x7080f400, 0x1e78b910, 0xd1f41e07, 0x2001b90f, 0xf000e7c0, 0x2000f88f, 0x0000e7bc, 0x40010414,
    0x4604b570, 0x4616460d, 0xff44f7ff, 0xbd702000, 0x4604b570, 0x4616460d, 0x46294632, 0xf7ff4620,
    0xbd70ff67, 0x4604b510, 0xfe9cf7ff, 0xbd102000, 0x4604b5f0, 0x2300460d, 0x27002600, 0x21004626,
    0xf856e007, 0x6810cb04, 0xd0004584, 0x1d12e004, 0xebb11c49, 0xd3f40f95, 0x4637bf00, 0xe0062300,
    0xcb01f817, 0x45845cd0, 0xe004d000, 0xf0051c5b, 0x42980003, 0xbf00d8f4, 0x0081eb04, 0xbdf04418,
    0x1e01bf00, 0x0001f1a0, 0x4770d1fb, 0x481fb510, 0x481f6802, 0xf3c06800, 0x481d0481, 0xf3c06800,
    0xb90c2303, 0xe0081192, 0xd1012c01, 0xe0041292, 0xd1012c02, 0xe0001312, 0xb10b1392, 0xd1022b0f,
    0xf83af000, 0xf003e020, 0xb1180001, 0xf000b9e2, 0xe019f833, 0x0002f003, 0xd1042802, 0xd1132a01,
    0xf82af000, 0xf003e010, 0x28040004, 0x2a02d104, 0xf000d10a, 0xe007f821, 0x0008f003, 0xd1032808,
    0xd1012a03, 0xf818f000, 0x0000bd10, 0x40049404, 0x40010680, 0x4807b500, 0xf3c06800, 0xb9084000,
    0xf816f000, 0x68004803, 0x0001f000, 0xf7ffb908, 0xbd00ffad, 0x40010680, 0x49034802, 0x48036008,
    0x47706008, 0xffff0123, 0x40049408, 0xffff3210, 0x4823b510, 0xb2926842, 0x68004822, 0x4481f3c0,
    0x68004820, 0x6303f3c0, 0x1192b90c, 0x2c01e008, 0x1292d101, 0x2c02e004, 0x1312d101, 0x1392e000,
    0x2001b90b, 0x2000e000, 0xd1012b0f, 0xe0002101, 0x43082100, 0xf000b110, 0xe020f827, 0x0001f003,
    0xb9e2b118, 0xf820f000, 0xf003e019, 0x28020002, 0x2a01d104, 0xf000d113, 0xe010f817, 0x0004f003,
    0xd1042804, 0xd10a2a02, 0xf80ef000, 0xf003e007, 0x28080008, 0x2a03d103, 0xf000d101, 0xbd10f805,
    0x40049000, 0x40010680, 0x49034802, 0x48036088, 0x47706088, 0xffff0123, 0x40049000, 0xffff3210,
    0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x200003a5,
    'pc_unInit': 0x200003c9,
    'pc_program_page': 0x200003b5,
    'pc_erase_sector': 0x200000fb,
    'pc_eraseAll': 0x200000f3,

    'static_base' : 0x20000000 + 0x00000020 + 0x000004b0,
    'begin_stack' : 0x20000700,
    'begin_data' : 0x20000000 + 0x1000,
    'page_size' : 0x200,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    'page_buffers' : [0x20001000, 0x20001200],   # Enable double buffering
    'min_program_length' : 0x200,
}


FLASH_ALGO_OTP = {
    'load_address' : 0x20000000,

    # Flash algorithm as a hex string
    'instructions': [
    0xE00ABE00, 
    0x4770ba40, 0x4770bac0, 0x0030ea4f, 0x00004770, 0x5001f24a, 0x8008490a, 0x7800480a, 0x0007f020,
    0x39264908, 0x0026f881, 0x68004807, 0x00f0f020, 0x60084905, 0x49032001, 0x70081d09, 0x00004770,
    0x4005440e, 0x40054026, 0x40010408, 0x5101f24a, 0x80114a16, 0x6a094916, 0x0170f021, 0x4a143110,
    0xf2406211, 0x68094104, 0x0001f001, 0x4911b150, 0x60114a11, 0x68094911, 0x01f0f021, 0x4a0f3140,
    0xe0096011, 0x4a0c490e, 0x490c6011, 0xf0216809, 0x315001f0, 0x60114a09, 0x4a052100, 0x7011322a,
    0x4a032105, 0x1026f882, 0x00004770, 0x4005440e, 0x40054000, 0x10102781, 0x4005410c, 0x40010408,
    0x10101f81, 0x4603b570, 0xe003460c, 0x5b01f814, 0x5b01f803, 0xf1a21e15, 0xd1f70201, 0xb510bd70,
    0xf81ef000, 0xb510bd10, 0x46204604, 0xf81af000, 0x0000bd10, 0xf000b500, 0x4808f959, 0xf4206800,
    0x49067080, 0x20016008, 0x20006008, 0x1e406008, 0x390c4902, 0xf0006008, 0xbd00f949, 0x4001040c,
    0x47702000, 0x20004601, 0x00004770, 0x4811b500, 0x60084911, 0x60084811, 0x300c480f, 0xf4206800,
    0xf5007080, 0x490c7080, 0x6008310c, 0x5001f24a, 0x8008490b, 0x6a00480b, 0x40e0f420, 0x40c0f500,
    0x62084908, 0x4025f44f, 0x80084905, 0xf91ef000, 0x0000bd00, 0xffff0123, 0x40010400, 0xffff3210,
    0x4005440e, 0x40054000, 0x45f8e92d, 0x460c4680, 0xf04f4615, 0x900030ff, 0x4740f649, 0x493d203f,
    0xf0006008, 0x483bf903, 0x68003808, 0x0001f020, 0x49381c40, 0x60083908, 0x68004608, 0x0070f020,
    0x60083030, 0x68004608, 0x7080f420, 0x7080f500, 0x46466008, 0xf000bf00, 0xf04ff8e9, 0xe0260a00,
    0x4740f649, 0x60306828, 0x1d2d1d36, 0xf8def000, 0xf000e001, 0x4827f8db, 0x68001f00, 0x0010f000,
    0x1e78b910, 0xd1f41e07, 0x2001b917, 0x85f8e8bd, 0x1f004820, 0xf0006800, 0xb118000f, 0xf8c6f000,
    0xe7f32001, 0x491b2010, 0xf10a6008, 0xebba0a01, 0xd3d50f94, 0x0003f004, 0xf004b138, 0x46290203,
    0xf7ff4668, 0x9800ff3f, 0xf000c601, 0x4811f8af, 0x68003808, 0x0070f020, 0x3908490e, 0x46086008,
    0xf0206800, 0x60080001, 0x4740f649, 0xf000e001, 0x4808f89d, 0x68001f00, 0x7080f400, 0x1e78b910,
    0xd1f41e07, 0x2001b90f, 0xf000e7c0, 0x2000f88f, 0x0000e7bc, 0x40010414, 0x4604b570, 0x4616460d,
    0xff44f7ff, 0xbd702000, 0x4604b570, 0x4616460d, 0x46294632, 0xf7ff4620, 0xbd70ff67, 0x4604b510,
    0xff18f7ff, 0xbd102000, 0x4604b5f0, 0x2300460d, 0x27002600, 0x21004626, 0xf856e007, 0x6810cb04,
    0xd0004584, 0x1d12e004, 0xebb11c49, 0xd3f40f95, 0x4637bf00, 0xe0062300, 0xcb01f817, 0x45845cd0,
    0xe004d000, 0xf0051c5b, 0x42980003, 0xbf00d8f4, 0x0081eb04, 0xbdf04418, 0x1e01bf00, 0x0001f1a0,
    0x4770d1fb, 0x481fb510, 0x481f6802, 0xf3c06800, 0x481d0481, 0xf3c06800, 0xb90c2303, 0xe0081192,
    0xd1012c01, 0xe0041292, 0xd1012c02, 0xe0001312, 0xb10b1392, 0xd1022b0f, 0xf83af000, 0xf003e020,
    0xb1180001, 0xf000b9e2, 0xe019f833, 0x0002f003, 0xd1042802, 0xd1132a01, 0xf82af000, 0xf003e010,
    0x28040004, 0x2a02d104, 0xf000d10a, 0xe007f821, 0x0008f003, 0xd1032808, 0xd1012a03, 0xf818f000,
    0x0000bd10, 0x40049404, 0x40010680, 0x4807b500, 0xf3c06800, 0xb9084000, 0xf816f000, 0x68004803,
    0x0001f000, 0xf7ffb908, 0xbd00ffad, 0x40010680, 0x49034802, 0x48036008, 0x47706008, 0xffff0123,
    0x40049408, 0xffff3210, 0x4823b510, 0xb2926842, 0x68004822, 0x4481f3c0, 0x68004820, 0x6303f3c0,
    0x1192b90c, 0x2c01e008, 0x1292d101, 0x2c02e004, 0x1312d101, 0x1392e000, 0x2001b90b, 0x2000e000,
    0xd1012b0f, 0xe0002101, 0x43082100, 0xf000b110, 0xe020f827, 0x0001f003, 0xb9e2b118, 0xf820f000,
    0xf003e019, 0x28020002, 0x2a01d104, 0xf000d113, 0xe010f817, 0x0004f003, 0xd1042804, 0xd10a2a02,
    0xf80ef000, 0xf003e007, 0x28080008, 0x2a03d103, 0xf000d101, 0xbd10f805, 0x40049000, 0x40010680,
    0x49034802, 0x48036088, 0x47706088, 0xffff0123, 0x40049000, 0xffff3210, 0x00000000
    ],

    # Relative function addresses
    'pc_init': 0x2000029d,
    'pc_unInit': 0x200002c1,
    'pc_program_page': 0x200002ad,
    'pc_erase_sector': 0x200000eb,
    'pc_eraseAll': 0x200000e3,

    'static_base' : 0x20000000 + 0x00000004 + 0x00000498,
    'begin_stack' : 0x20000700,
    'begin_data' : 0x20000000 + 0x1000,
    'page_size' : 0x3fc,
    'analyzer_supported' : False,
    'analyzer_address' : 0x00000000,
    'page_buffers' : [0x20001000, 0x200013fc],   # Enable double buffering
    'min_program_length' : 0x3fc,

    # Flash information
    'flash_start': 0x3000c00,
    'flash_size': 0x3fc,
    'sector_sizes': (
        (0x0, 0x3fc),
    )
}


class HC32F451xC(CoreSightTarget):

    VENDOR = "HDSC"

    MEMORY_MAP = MemoryMap(
        FlashRegion( start=0x00000000, length=0x40000, page_size=0x200, sector_size=0x2000,
                        is_boot_memory=True,
                        algo=FLASH_ALGO),
        FlashRegion( start=0x03000C00, length=0x3FC, sector_size=0x3FC,
                        is_boot_memory=False,
                        is_default=False,
                        algo=FLASH_ALGO_OTP),
        RamRegion(   start=0x1FFF8000, length=0x2F000),
        RamRegion(   start=0x200F0000, length=0x1000)
        )

    def __init__(self, session):
        super(HC32F451xC, self).__init__(session, self.MEMORY_MAP)
        self._svd_location = SVDFile.from_builtin("HC32F460.svd")

    def post_connect_hook(self):
        self.write32(DBGMCU.STCTL, DBGMCU.STCTL_VALUE)
        self.write32(DBGMCU.TRACECTL, DBGMCU.TRACECTL_VALUE)


class HC32F451xE(CoreSightTarget):

    VENDOR = "HDSC"

    MEMORY_MAP = MemoryMap(
        FlashRegion( start=0x00000000, length=0x80000, page_size=0x200, sector_size=0x2000,
                        is_boot_memory=True,
                        algo=FLASH_ALGO),
        FlashRegion( start=0x03000C00, length=0x3FC, sector_size=0x3FC,
                        is_boot_memory=False,
                        is_default=False,
                        algo=FLASH_ALGO_OTP),
        RamRegion(   start=0x1FFF8000, length=0x2F000),
        RamRegion(   start=0x200F0000, length=0x1000)
        )

    def __init__(self, session):
        super(HC32F451xE, self).__init__(session, self.MEMORY_MAP)
        self._svd_location = SVDFile.from_builtin("HC32F460.svd")

    def post_connect_hook(self):
        self.write32(DBGMCU.STCTL, DBGMCU.STCTL_VALUE)
        self.write32(DBGMCU.TRACECTL, DBGMCU.TRACECTL_VALUE)


class HC32F452xC(CoreSightTarget):

    VENDOR = "HDSC"

    MEMORY_MAP = MemoryMap(
        FlashRegion( start=0x00000000, length=0x40000, page_size=0x200, sector_size=0x2000,
                        is_boot_memory=True,
                        algo=FLASH_ALGO),
        FlashRegion( start=0x03000C00, length=0x3FC, sector_size=0x3FC,
                        is_boot_memory=False,
                        is_default=False,
                        algo=FLASH_ALGO_OTP),
        RamRegion(   start=0x1FFF8000, length=0x2F000),
        RamRegion(   start=0x200F0000, length=0x1000)
        )

    def __init__(self, session):
        super(HC32F452xC, self).__init__(session, self.MEMORY_MAP)
        self._svd_location = SVDFile.from_builtin("HC32F460.svd")

    def post_connect_hook(self):
        self.write32(DBGMCU.STCTL, DBGMCU.STCTL_VALUE)
        self.write32(DBGMCU.TRACECTL, DBGMCU.TRACECTL_VALUE)


class HC32F452xE(CoreSightTarget):

    VENDOR = "HDSC"

    MEMORY_MAP = MemoryMap(
        FlashRegion( start=0x00000000, length=0x80000, page_size=0x200, sector_size=0x2000,
                        is_boot_memory=True,
                        algo=FLASH_ALGO),
        FlashRegion( start=0x03000C00, length=0x3FC, sector_size=0x3FC,
                        is_boot_memory=False,
                        is_default=False,
                        algo=FLASH_ALGO_OTP),
        RamRegion(   start=0x1FFF8000, length=0x2F000),
        RamRegion(   start=0x200F0000, length=0x1000)
        )

    def __init__(self, session):
        super(HC32F452xE, self).__init__(session, self.MEMORY_MAP)
        self._svd_location = SVDFile.from_builtin("HC32F460.svd")

    def post_connect_hook(self):
        self.write32(DBGMCU.STCTL, DBGMCU.STCTL_VALUE)
        self.write32(DBGMCU.TRACECTL, DBGMCU.TRACECTL_VALUE)

