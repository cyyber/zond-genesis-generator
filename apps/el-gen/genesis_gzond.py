import json
import ruamel.yaml as yaml
import sys

testnet_config_path = "genesis-config.yaml"
mainnet_config_path = "/apps/el-gen/mainnet/genesis.json"
isNamedTestnet = False
combined_allocs = {}
if len(sys.argv) > 1:
    testnet_config_path = sys.argv[1]

with open(testnet_config_path) as stream:
    data = yaml.safe_load(stream)

# if int(data['chain_id']) == 1 or int(data['chain_id']) == 11155111:
if int(data['chain_id']) == 1:
    isNamedTestnet = True

if int(data['chain_id']) == 1:
    # TODO(now.youtrack.cloud/issue/TQ-37)
    with open(mainnet_config_path) as m:
        mainnet_json = json.loads(m.read())
    out = mainnet_json
else:
    out = {
        "config": {
            "chainId": int(data['chain_id'])
        },
        "alloc": {
            # Allocate 1 wei to all possible pre-compiles.
            # See https://github.com/ethereum/EIPs/issues/716 "SpuriousDragon RIPEMD bug"
            # E.g. Rinkeby allocates it like this.
            # See https://github.com/ethereum/go-ethereum/blob/092856267067dd78b527a773f5b240d5c9f5693a/core/genesis.go#L370
            **{
                "Z" + i.to_bytes(length=20, byteorder='big').hex(): {
                    "balance": "1",
                } for i in range(256)
            },
            # deposit contract
            data['deposit_contract_address']: {
                "balance": "0",
                "code": "0x60806040526004361061003e575f3560e01c806301ffc9a714610042578063228951181461007e578063621fd1301461009a578063c5f2892f146100c4575b5f80fd5b34801561004d575f80fd5b5061006860048036038101906100639190610b67565b6100ee565b6040516100759190610bac565b60405180910390f35b61009860048036038101906100939190610c59565b6101bf565b005b3480156100a5575f80fd5b506100ae6105fb565b6040516100bb9190610da7565b60405180910390f35b3480156100cf575f80fd5b506100d861060d565b6040516100e59190610dd6565b60405180910390f35b5f7f01ffc9a7000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff191614806101b857507f85640907000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916145b9050919050565b610a208787905014610206576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101fd90610e6f565b60405180910390fd5b6020858590501461024c576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161024390610efd565b60405180910390fd5b6111f38383905014610293576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161028a90610f8b565b60405180910390fd5b670de0b6b3a76400003410156102de576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016102d590611019565b60405180910390fd5b5f633b9aca00346102ef919061106d565b1461032f576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016103269061110d565b60405180910390fd5b5f633b9aca00346103409190611158565b905067ffffffffffffffff801681111561038f576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610386906111f8565b60405180910390fd5b5f610399826107dd565b90507f649bbc62d0e31342afea4e5cd82d4049e7e1ee912fc0889aa790803be39038c589898989858a8a6103ce6020546107dd565b6040516103e2989796959493929190611250565b60405180910390a15f60018a8a8a8a868b8b6040516104079796959493929190611328565b602060405180830381855afa158015610422573d5f803e3d5ffd5b5050506040513d601f19601f82011682018060405250810190610445919061137f565b9050838114610489576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161048090611440565b60405180910390fd5b600160206002610499919061158d565b6104a391906115d7565b602054106104e6576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016104dd9061167a565b60405180910390fd5b600160205f8282546104f89190611698565b925050819055505f60205490505f5b60208110156105de5760018083160361053d57825f826020811061052e5761052d6116cb565b5b018190555050505050506105f2565b60025f8260208110610552576105516116cb565b5b015484604051602001610566929190611718565b6040516020818303038152906040526040516105829190611743565b602060405180830381855afa15801561059d573d5f803e3d5ffd5b5050506040513d601f19601f820116820180604052508101906105c0919061137f565b92506002826105cf9190611158565b91508080600101915050610507565b505f6105ed576105ec611759565b5b505050505b50505050505050565b60606106086020546107dd565b905090565b5f805f60205490505f5b6020811015610757576001808316036106b45760025f826020811061063f5761063e6116cb565b5b015484604051602001610653929190611718565b60405160208183030381529060405260405161066f9190611743565b602060405180830381855afa15801561068a573d5f803e3d5ffd5b5050506040513d601f19601f820116820180604052508101906106ad919061137f565b925061073b565b600283602183602081106106cb576106ca6116cb565b5b01546040516020016106de929190611718565b6040516020818303038152906040526040516106fa9190611743565b602060405180830381855afa158015610715573d5f803e3d5ffd5b5050506040513d601f19601f82011682018060405250810190610738919061137f565b92505b6002826107489190611158565b91508080600101915050610617565b506002826107666020546107dd565b5f60401b60405160200161077c939291906117d1565b6040516020818303038152906040526040516107989190611743565b602060405180830381855afa1580156107b3573d5f803e3d5ffd5b5050506040513d601f19601f820116820180604052508101906107d6919061137f565b9250505090565b6060600867ffffffffffffffff8111156107fa576107f9611809565b5b6040519080825280601f01601f19166020018201604052801561082c5781602001600182028036833780820191505090505b5090505f8260c01b90508060076008811061084a576108496116cb565b5b1a60f81b825f81518110610861576108606116cb565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690815f1a905350806006600881106108a3576108a26116cb565b5b1a60f81b826001815181106108bb576108ba6116cb565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690815f1a905350806005600881106108fd576108fc6116cb565b5b1a60f81b82600281518110610915576109146116cb565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690815f1a90535080600460088110610957576109566116cb565b5b1a60f81b8260038151811061096f5761096e6116cb565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690815f1a905350806003600881106109b1576109b06116cb565b5b1a60f81b826004815181106109c9576109c86116cb565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690815f1a90535080600260088110610a0b57610a0a6116cb565b5b1a60f81b82600581518110610a2357610a226116cb565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690815f1a90535080600160088110610a6557610a646116cb565b5b1a60f81b82600681518110610a7d57610a7c6116cb565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690815f1a905350805f60088110610abe57610abd6116cb565b5b1a60f81b82600781518110610ad657610ad56116cb565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191690815f1a90535050919050565b5f80fd5b5f80fd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b610b4681610b12565b8114610b50575f80fd5b50565b5f81359050610b6181610b3d565b92915050565b5f60208284031215610b7c57610b7b610b0a565b5b5f610b8984828501610b53565b91505092915050565b5f8115159050919050565b610ba681610b92565b82525050565b5f602082019050610bbf5f830184610b9d565b92915050565b5f80fd5b5f80fd5b5f80fd5b5f8083601f840112610be657610be5610bc5565b5b8235905067ffffffffffffffff811115610c0357610c02610bc9565b5b602083019150836001820283011115610c1f57610c1e610bcd565b5b9250929050565b5f819050919050565b610c3881610c26565b8114610c42575f80fd5b50565b5f81359050610c5381610c2f565b92915050565b5f805f805f805f6080888a031215610c7457610c73610b0a565b5b5f88013567ffffffffffffffff811115610c9157610c90610b0e565b5b610c9d8a828b01610bd1565b9750975050602088013567ffffffffffffffff811115610cc057610cbf610b0e565b5b610ccc8a828b01610bd1565b9550955050604088013567ffffffffffffffff811115610cef57610cee610b0e565b5b610cfb8a828b01610bd1565b93509350506060610d0e8a828b01610c45565b91505092959891949750929550565b5f81519050919050565b5f82825260208201905092915050565b5f5b83811015610d54578082015181840152602081019050610d39565b5f8484015250505050565b5f601f19601f8301169050919050565b5f610d7982610d1d565b610d838185610d27565b9350610d93818560208601610d37565b610d9c81610d5f565b840191505092915050565b5f6020820190508181035f830152610dbf8184610d6f565b905092915050565b610dd081610c26565b82525050565b5f602082019050610de95f830184610dc7565b92915050565b5f82825260208201905092915050565b7f4465706f736974436f6e74726163743a20696e76616c6964207075626b6579205f8201527f6c656e6774680000000000000000000000000000000000000000000000000000602082015250565b5f610e59602683610def565b9150610e6482610dff565b604082019050919050565b5f6020820190508181035f830152610e8681610e4d565b9050919050565b7f4465706f736974436f6e74726163743a20696e76616c696420776974686472615f8201527f77616c5f63726564656e7469616c73206c656e67746800000000000000000000602082015250565b5f610ee7603683610def565b9150610ef282610e8d565b604082019050919050565b5f6020820190508181035f830152610f1481610edb565b9050919050565b7f4465706f736974436f6e74726163743a20696e76616c6964207369676e6174755f8201527f7265206c656e6774680000000000000000000000000000000000000000000000602082015250565b5f610f75602983610def565b9150610f8082610f1b565b604082019050919050565b5f6020820190508181035f830152610fa281610f69565b9050919050565b7f4465706f736974436f6e74726163743a206465706f7369742076616c756520745f8201527f6f6f206c6f770000000000000000000000000000000000000000000000000000602082015250565b5f611003602683610def565b915061100e82610fa9565b604082019050919050565b5f6020820190508181035f83015261103081610ff7565b9050919050565b5f819050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601260045260245ffd5b5f61107782611037565b915061108283611037565b92508261109257611091611040565b5b828206905092915050565b7f4465706f736974436f6e74726163743a206465706f7369742076616c7565206e5f8201527f6f74206d756c7469706c65206f66206777656900000000000000000000000000602082015250565b5f6110f7603383610def565b91506111028261109d565b604082019050919050565b5f6020820190508181035f830152611124816110eb565b9050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f61116282611037565b915061116d83611037565b92508261117d5761117c611040565b5b828204905092915050565b7f4465706f736974436f6e74726163743a206465706f7369742076616c756520745f8201527f6f6f206869676800000000000000000000000000000000000000000000000000602082015250565b5f6111e2602783610def565b91506111ed82611188565b604082019050919050565b5f6020820190508181035f83015261120f816111d6565b9050919050565b828183375f83830152505050565b5f61122f8385610d27565b935061123c838584611216565b61124583610d5f565b840190509392505050565b5f60a0820190508181035f830152611269818a8c611224565b9050818103602083015261127e81888a611224565b905081810360408301526112928187610d6f565b905081810360608301526112a7818587611224565b905081810360808301526112bb8184610d6f565b90509998505050505050505050565b5f81905092915050565b5f6112df83856112ca565b93506112ec838584611216565b82840190509392505050565b5f61130282610d1d565b61130c81856112ca565b935061131c818560208601610d37565b80840191505092915050565b5f61133482898b6112d4565b91506113418287896112d4565b915061134d82866112f8565b915061135a8284866112d4565b915081905098975050505050505050565b5f8151905061137981610c2f565b92915050565b5f6020828403121561139457611393610b0a565b5b5f6113a18482850161136b565b91505092915050565b7f4465706f736974436f6e74726163743a207265636f6e737472756374656420445f8201527f65706f7369744461746120646f6573206e6f74206d6174636820737570706c6960208201527f6564206465706f7369745f646174615f726f6f74000000000000000000000000604082015250565b5f61142a605483610def565b9150611435826113aa565b606082019050919050565b5f6020820190508181035f8301526114578161141e565b9050919050565b5f8160011c9050919050565b5f808291508390505b60018511156114b35780860481111561148f5761148e61112b565b5b600185161561149e5780820291505b80810290506114ac8561145e565b9450611473565b94509492505050565b5f826114cb5760019050611586565b816114d8575f9050611586565b81600181146114ee57600281146114f857611527565b6001915050611586565b60ff84111561150a5761150961112b565b5b8360020a9150848211156115215761152061112b565b5b50611586565b5060208310610133831016604e8410600b841016171561155c5782820a9050838111156115575761155661112b565b5b611586565b611569848484600161146a565b925090508184048111156115805761157f61112b565b5b81810290505b9392505050565b5f61159782611037565b91506115a283611037565b92506115cf7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff84846114bc565b905092915050565b5f6115e182611037565b91506115ec83611037565b92508282039050818111156116045761160361112b565b5b92915050565b7f4465706f736974436f6e74726163743a206d65726b6c6520747265652066756c5f8201527f6c00000000000000000000000000000000000000000000000000000000000000602082015250565b5f611664602183610def565b915061166f8261160a565b604082019050919050565b5f6020820190508181035f83015261169181611658565b9050919050565b5f6116a282611037565b91506116ad83611037565b92508282019050808211156116c5576116c461112b565b5b92915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b5f819050919050565b61171261170d82610c26565b6116f8565b82525050565b5f6117238285611701565b6020820191506117338284611701565b6020820191508190509392505050565b5f61174e82846112f8565b915081905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52600160045260245ffd5b5f7fffffffffffffffffffffffffffffffffffffffffffffffff000000000000000082169050919050565b5f819050919050565b6117cb6117c682611786565b6117b1565b82525050565b5f6117dc8286611701565b6020820191506117ec82856112f8565b91506117f882846117ba565b601882019150819050949350505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffdfea26469706673582212208cf05207a6162d75b387c2e7ffc430b6ab230c92183c7073abb208002a440f9c64736f6c637829302e382e32332d646576656c6f702e323032342e31302e32362b636f6d6d69742e3835343135613239005a",
                "storage": {
                    "0x0000000000000000000000000000000000000000000000000000000000000022": "0xf5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b",
                    "0x0000000000000000000000000000000000000000000000000000000000000023": "0xdb56114e00fdd4c1f85c892bf35ac9a89289aaecb1ebd0a96cde606a748b5d71",
                    "0x0000000000000000000000000000000000000000000000000000000000000024": "0xc78009fdf07fc56a11f122370658a353aaa542ed63e44c4bc15ff4cd105ab33c",
                    "0x0000000000000000000000000000000000000000000000000000000000000025": "0x536d98837f2dd165a55d5eeae91485954472d56f246df256bf3cae19352a123c",
                    "0x0000000000000000000000000000000000000000000000000000000000000026": "0x9efde052aa15429fae05bad4d0b1d7c64da64d03d7a1854a588c2cb8430c0d30",
                    "0x0000000000000000000000000000000000000000000000000000000000000027": "0xd88ddfeed400a8755596b21942c1497e114c302e6118290f91e6772976041fa1",
                    "0x0000000000000000000000000000000000000000000000000000000000000028": "0x87eb0ddba57e35f6d286673802a4af5975e22506c7cf4c64bb6be5ee11527f2c",
                    "0x0000000000000000000000000000000000000000000000000000000000000029": "0x26846476fd5fc54a5d43385167c95144f2643f533cc85bb9d16b782f8d7db193",
                    "0x000000000000000000000000000000000000000000000000000000000000002a": "0x506d86582d252405b840018792cad2bf1259f1ef5aa5f887e13cb2f0094f51e1",
                    "0x000000000000000000000000000000000000000000000000000000000000002b": "0xffff0ad7e659772f9534c195c815efc4014ef1e1daed4404c06385d11192e92b",
                    "0x000000000000000000000000000000000000000000000000000000000000002c": "0x6cf04127db05441cd833107a52be852868890e4317e6a02ab47683aa75964220",
                    "0x000000000000000000000000000000000000000000000000000000000000002d": "0xb7d05f875f140027ef5118a2247bbb84ce8f2f0f1123623085daf7960c329f5f",
                    "0x000000000000000000000000000000000000000000000000000000000000002e": "0xdf6af5f5bbdb6be9ef8aa618e4bf8073960867171e29676f8b284dea6a08a85e",
                    "0x000000000000000000000000000000000000000000000000000000000000002f": "0xb58d900f5e182e3c50ef74969ea16c7726c549757cc23523c369587da7293784",
                    "0x0000000000000000000000000000000000000000000000000000000000000030": "0xd49a7502ffcfb0340b1d7885688500ca308161a7f96b62df9d083b71fcc8f2bb",
                    "0x0000000000000000000000000000000000000000000000000000000000000031": "0x8fe6b1689256c0d385f42f5bbe2027a22c1996e110ba97c171d3e5948de92beb",
                    "0x0000000000000000000000000000000000000000000000000000000000000032": "0x8d0d63c39ebade8509e0ae3c9c3876fb5fa112be18f905ecacfecb92057603ab",
                    "0x0000000000000000000000000000000000000000000000000000000000000033": "0x95eec8b2e541cad4e91de38385f2e046619f54496c2382cb6cacd5b98c26f5a4",
                    "0x0000000000000000000000000000000000000000000000000000000000000034": "0xf893e908917775b62bff23294dbbe3a1cd8e6cc1c35b4801887b646a6f81f17f",
                    "0x0000000000000000000000000000000000000000000000000000000000000035": "0xcddba7b592e3133393c16194fac7431abf2f5485ed711db282183c819e08ebaa",
                    "0x0000000000000000000000000000000000000000000000000000000000000036": "0x8a8d7fe3af8caa085a7639a832001457dfb9128a8061142ad0335629ff23ff9c",
                    "0x0000000000000000000000000000000000000000000000000000000000000037": "0xfeb3c337d7a51a6fbf00b9e34c52e1c9195c969bd4e7a0bfd51d5c5bed9c1167",
                    "0x0000000000000000000000000000000000000000000000000000000000000038": "0xe71f0aa83cc32edfbefa9f4d3e0174ca85182eec9f3a09f6a6c0df6377a510d7",
                    "0x0000000000000000000000000000000000000000000000000000000000000039": "0x31206fa80a50bb6abe29085058f16212212a60eec8f049fecb92d8c8e0a84bc0",
                    "0x000000000000000000000000000000000000000000000000000000000000003a": "0x21352bfecbeddde993839f614c3dac0a3ee37543f9b412b16199dc158e23b544",
                    "0x000000000000000000000000000000000000000000000000000000000000003b": "0x619e312724bb6d7c3153ed9de791d764a366b389af13c58bf8a8d90481a46765",
                    "0x000000000000000000000000000000000000000000000000000000000000003c": "0x7cdd2986268250628d0c10e385c58c6191e6fbe05191bcc04f133f2cea72c1c4",
                    "0x000000000000000000000000000000000000000000000000000000000000003d": "0x848930bd7ba8cac54661072113fb278869e07bb8587f91392933374d017bcbe1",
                    "0x000000000000000000000000000000000000000000000000000000000000003e": "0x8869ff2c22b28cc10510d9853292803328be4fb0e80495e8bb8d271f5b889636",
                    "0x000000000000000000000000000000000000000000000000000000000000003f": "0xb5fe28e79f1b850f8658246ce9b6a1e7b49fc06db7143e8fe0b4f2b0c5523a5c",
                    "0x0000000000000000000000000000000000000000000000000000000000000040": "0x985e929f70af28d0bdd1a90a808f977f597c7c778c489e98d3bd8910d31ac0f7"
                }
            }
        },
        "coinbase": "Z0000000000000000000000000000000000000000",
        "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "gasLimit": hex(int(data['genesis_gaslimit'] if 'genesis_gaslimit' in data and data['genesis_gaslimit'] is not None else 25000000)),
        "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "timestamp": str(data['genesis_timestamp'])
    }
    
    # Some hardcoded addrs
    def add_alloc_entry(addr, account):
        # Convert balance format
        if isinstance(account, dict) and 'balance' in account:
            balance_value = account['balance'].replace('ETH', '0' * 18)
        else:
            # If it's not a dictionary, assume it's a single value for backward compatibility
            balance_value = account.replace('ETH', '0' * 18)

        # Create alloc dictionary entry
        alloc_entry = {"balance": balance_value}

        # Optionally add code
        if 'code' in account:
            alloc_entry['code'] = account['code']

        # Optionally add storage
        if 'storage' in account:
            alloc_entry['storage'] = account['storage']

        # Optionally set nonce
        if 'nonce' in account:
            alloc_entry['nonce'] = account['nonce']

        # TODO(rgeraldes24)
        # Optionally set private key
        if 'secretKey' in account:
            alloc_entry['secretKey'] = account['secretKey']

        # Add alloc entry to output's alloc field
        out["alloc"][addr] = alloc_entry

    for addr, account in data['el_premine_addrs'].items():
        add_alloc_entry(addr, account)

    for addr, account in data['additional_preloaded_contracts'].items():
        add_alloc_entry(addr, account)

print(json.dumps(out, indent='  '))
