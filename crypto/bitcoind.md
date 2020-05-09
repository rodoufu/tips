# bitcoind

## Start

```sh
bitcoind -daemon
```

## Stop

```sh
bitcoin-cli stop
```

## Get block info

```sh
bitcoin-cli getblockchaininfo
```

## Decode a transaction

```sh
bitcoin-cli decoderawtransaction 01000000015b9d744cb3a6b661fdfac60e2af7a54d8abdaf8f1c0fcb028ab369b041c6f1360000000000ffffffff0201000000000000001976a91409e4bc6b434b1efbaa6e5087f9342bc070b2086888ac4dd8aa4c000000001976a914e0ad60c897901128662623c500a4a6079e99cd3e88ac00000000
```

And the response should be:
```js
{
  "txid": "9a6f65737993d6237643f783e2ac09bd07af8cb93b5698596583b056ced4aa1c",
  "hash": "9a6f65737993d6237643f783e2ac09bd07af8cb93b5698596583b056ced4aa1c",
  "version": 1,
  "size": 119,
  "vsize": 119,
  "weight": 476,
  "locktime": 0,
  "vin": [
    {
      "txid": "36f1c641b069b38a02cb0f1c8fafbd8a4da5f72a0ec6fafd61b6a6b34c749d5b",
      "vout": 0,
      "scriptSig": {
        "asm": "",
        "hex": ""
      },
      "sequence": 4294967295
    }
  ],
  "vout": [
    {
      "value": 0.00000001,
      "n": 0,
      "scriptPubKey": {
        "asm": "OP_DUP OP_HASH160 09e4bc6b434b1efbaa6e5087f9342bc070b20868 OP_EQUALVERIFY OP_CHECKSIG",
        "hex": "76a91409e4bc6b434b1efbaa6e5087f9342bc070b2086888ac",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": [
          "1uK6apqqbRQs1bSnzxq2dE26cpxVbGDjh"
        ]
      }
    },
    {
      "value": 12.86264909,
      "n": 1,
      "scriptPubKey": {
        "asm": "OP_DUP OP_HASH160 e0ad60c897901128662623c500a4a6079e99cd3e OP_EQUALVERIFY OP_CHECKSIG",
        "hex": "76a914e0ad60c897901128662623c500a4a6079e99cd3e88ac",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": [
          "1MUz4VMYui5qY1mxUiG8BQ1Luv6tqkvaiL"
        ]
      }
    }
  ]
}
```
