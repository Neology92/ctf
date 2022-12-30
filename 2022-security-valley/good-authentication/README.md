- password must have 12 chars
- sliced into 3 blocks of 4 chars
- every block iterated, chard converted to ASCII values and XORed by specific no: 7, 11, 12 (each for specific block), next converted to ASCII

- just invert the process. Can actually use the original code, as XOR is invertable by itself

```
$ curl -X POST http://ctf.securityvalley.org:7777/api/v1/validate -H 'Content-Type: application/json' -d '{"pass": "this_is_cool"}'
```
