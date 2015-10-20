"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash_kinetis import Flash_Kinetis

flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4831b510, 0x6041492f, 0x60814930, 0x22806801, 0x22204391, 0x60014311, 0x4448482d, 0xf8cef000,
    0xd0002800, 0xbd102001, 0x47702000, 0xb5104828, 0x44484928, 0xf8aef000, 0xd1050004, 0x21004824,
    0xf0004448, 0x4604f983, 0xf835f000, 0xbd104620, 0x4d1fb570, 0x444d4606, 0x4b1e4601, 0x68ea4628,
    0xf85ef000, 0xd1060004, 0x46312300, 0x68ea4628, 0xf934f000, 0xf0004604, 0x4620f81e, 0xb5febd70,
    0x460b460d, 0x46014607, 0x46164811, 0xf0004448, 0x0004f8f5, 0x9001d10b, 0x21019002, 0x9100480c,
    0x462a4633, 0x44484639, 0xf95ef000, 0xf0004604, 0x4620f802, 0x4808bdfe, 0x220168c1, 0x43110292,
    0x477060c1, 0xd928c520, 0x40076000, 0x0000ffff, 0x00000004, 0x6b65666b, 0xf0003000, 0x2800b500,
    0x2a00d009, 0x000bd007, 0xfa35f000, 0x0b0b0708, 0x13110f0d, 0x20041715, 0x68c0bd00, 0x20006010,
    0x6840bd00, 0x6880e7fa, 0x6800e7f8, 0x2001e7f6, 0x6900e7f4, 0x6940e7f2, 0x206ae7f0, 0x0000bd00,
    0x4607b5f8, 0x460d4614, 0xf0004618, 0x2800f889, 0x2308d12a, 0x46294622, 0xf0004638, 0x0006f867,
    0x192cd122, 0x68f91e64, 0x91004620, 0xf956f000, 0xd0162900, 0x1c409c00, 0x1e644344, 0x480be011,
    0x68004478, 0x490a6005, 0x71c82009, 0xf92ef000, 0x69b84606, 0xd0002800, 0x2e004780, 0x68f8d103,
    0x42a51945, 0x4630d9eb, 0x0000bdf8, 0x0000042c, 0x40020000, 0x4604b510, 0xf0004608, 0x2800f851,
    0x2c00d106, 0x4904d005, 0x71c82044, 0xf90ef000, 0x2004bd10, 0x0000bd10, 0x40020000, 0x2800b510,
    0x492ad019, 0x4a2a68c9, 0x00490e09, 0x5a51447a, 0xd0120309, 0x60022200, 0x21026041, 0x02896081,
    0x492460c1, 0x158b7a0c, 0x610340a3, 0x61827ac9, 0x46106141, 0x2004bd10, 0x2064bd10, 0x2800bd10,
    0x6181d002, 0x47702000, 0x47702004, 0x2800b510, 0x1e5bd004, 0x421c460c, 0xe001d104, 0xbd102004,
    0xd001421a, 0xbd102065, 0x428b6803, 0x6840d804, 0x18181889, 0xd2014288, 0xbd102066, 0xbd102000,
    0x4288490d, 0x206bd001, 0x20004770, 0x28004770, 0x290fd008, 0x2a04d802, 0xe005d104, 0xd8012913,
    0xd0012a08, 0x47702004, 0x47702000, 0x40075040, 0x000003a0, 0x40020020, 0x6b65666b, 0xb081b5ff,
    0x0015461e, 0xd007460f, 0x46322304, 0xf7ff9801, 0x0004ffbd, 0xe018d101, 0xb0052004, 0x480dbdf0,
    0x68014478, 0xcd02600f, 0x60416800, 0x2006490a, 0xf00071c8, 0x4604f88b, 0x69809801, 0xd0002800,
    0x2c004780, 0x1d3fd103, 0x2e001f36, 0x4620d1e7, 0x0000e7e3, 0x000002ec, 0x40020000, 0xb081b5ff,
    0x460e4614, 0x23084605, 0xff90f7ff, 0xd1272800, 0x686868a9, 0xf882f000, 0x42719000, 0x40014240,
    0x42b5424d, 0x9800d101, 0x2c00182d, 0x1bafd017, 0xd90042a7, 0x480b4627, 0x447808f9, 0x60066800,
    0x22014809, 0x0a0a71c2, 0x728172c2, 0x72419904, 0xf84cf000, 0xd1032800, 0x19f61be4, 0x2000e7e3,
    0xbdf0b005, 0x00000272, 0x40020000, 0x2800b510, 0x4804d006, 0x71c22240, 0xf0007181, 0xbd10f837,
    0xbd102004, 0x40020000, 0x9f08b5f8, 0x4616001c, 0xd005460d, 0xf7ff2304, 0x2800ff49, 0xe01dd101,
    0xbdf82004, 0x4478480f, 0x600d6801, 0x2202490e, 0x9a0671ca, 0x680072ca, 0x60816821, 0xf816f000,
    0xd0082800, 0x29009907, 0x600dd000, 0xd0e82f00, 0x60392100, 0x1f36bdf8, 0x1d2d1d24, 0xd1e12e00,
    0x0000bdf8, 0x00000206, 0x40020000, 0x2170480a, 0x21807001, 0x78017001, 0xd5fc0609, 0x06817800,
    0x2067d501, 0x06c14770, 0x2068d501, 0x07c04770, 0x2069d0fc, 0x00004770, 0x40020000, 0x09032200,
    0xd32c428b, 0x428b0a03, 0x2300d311, 0xe04e469c, 0x430b4603, 0x2200d43c, 0x428b0843, 0x0903d331,
    0xd31c428b, 0x428b0a03, 0x4694d301, 0x09c3e03f, 0xd301428b, 0x1ac001cb, 0x09834152, 0xd301428b,
    0x1ac0018b, 0x09434152, 0xd301428b, 0x1ac0014b, 0x09034152, 0xd301428b, 0x1ac0010b, 0x08c34152,
    0xd301428b, 0x1ac000cb, 0x08834152, 0xd301428b, 0x1ac0008b, 0x08434152, 0xd301428b, 0x1ac0004b,
    0x1a414152, 0x4601d200, 0x46104152, 0xe05d4770, 0xd0000fca, 0x10034249, 0x4240d300, 0x22004053,
    0x0903469c, 0xd32d428b, 0x428b0a03, 0x22fcd312, 0xba120189, 0x428b0a03, 0x0189d30c, 0x428b1192,
    0x0189d308, 0x428b1192, 0x0189d304, 0x1192d03a, 0x0989e000, 0x428b09c3, 0x01cbd301, 0x41521ac0,
    0x428b0983, 0x018bd301, 0x41521ac0, 0x428b0943, 0x014bd301, 0x41521ac0, 0x428b0903, 0x010bd301,
    0x41521ac0, 0x428b08c3, 0x00cbd301, 0x41521ac0, 0x428b0883, 0x008bd301, 0x41521ac0, 0x0843d2d9,
    0xd301428b, 0x1ac0004b, 0x1a414152, 0x4601d200, 0x41524663, 0x4610105b, 0x4240d301, 0xd5002b00,
    0x47704249, 0x105b4663, 0x4240d300, 0x2000b501, 0x46c046c0, 0xb430bd02, 0x1e644674, 0x1c647825,
    0xd20042ab, 0x5d63461d, 0x18e3005b, 0x4718bc30, 0x00040002, 0x00080000, 0x00100000, 0x00200000,
    0x00400000, 0x00000080, 0x00000000, 0x00800000, 0x40020004, 0x00000000,
                                ],
               'pc_init' : 0x20000021,
               'pc_eraseAll' : 0x2000004D,
               'pc_erase_sector' : 0x20000071,
               'pc_program_page' : 0x2000009F,
               'begin_stack' : 0x20000800,
               'begin_data' : 0x20000a00,       # Analyzer uses a max of 2 KB data (512 pages * 4 bytes / page)
               'page_buffers' : [0x20000a00, 0x20001200],   # Enable double buffering
               'static_base' : 0x20000000 + 0x20 + 0x594,
               'min_program_length' : 8,
               'analyzer_supported' : True,
               'analyzer_address' : 0x1fffa000
              };

# @brief Flash algorithm for Kinetis L-series devices.
class Flash_kl28z(Flash_Kinetis):

    def __init__(self, target):
        super(Flash_kl28z, self).__init__(target, flash_algo)
