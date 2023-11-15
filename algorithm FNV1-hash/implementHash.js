
class KeyValuePair {
    key;
    value;
    constructor(_key, _value)
    {
    this.key = _key;
    this.value = _value;
    }
    getKey(){
    return(this.key);
    }

    getVal(){
        return(this.value);
    }
    setVal(New){
        this.value = New;
    }
}
class hashTable {
entries;
constructor()
{
this.entries =  [];
}
set(key, value)
{
let i;
for (i = 0; i < this.entries.length; i++)
{
if (this.entries[i].key == key)
{
this.entries[i].value = value;
return false;
}
}
this.entries.push(new KeyValuePair(key, value));
return true;
}
get(key)
{
let i = 0;
while(this.entries[i])
{
if (this.entries[i].key == key)
{
return this.entries[i].value;
}
i++;
}
}
remove(key)
{
let i;
for (i = 0; this.entries[i];i++)
{
if (this.entries[i].key == key)
{
this.entries.splice(i, 1);
return true
}
}
return false;
}
print()
{
let i = 0;
while(this.entries[i]){
i++;
}
console.log(`--------------------------------------------------------------\n =============== Size ${i} ==================\n--------------------------------------------------------------`);
i = 0;
while(this.entries[i])
{
console.log(`[${i}] ${this.entries[i].value}`);
i++;
}
console.log("==============================================================")
}
getHash(key) {
    const FnvOffsetBasis = 2166136261;
    const FNVPrime = 16777619;

    const encoder = new TextEncoder();
    const data = encoder.encode(key.toString());

    let hash = FnvOffsetBasis;

    for (let i = 0; i < data.length; i++) {
        hash ^= data[i];
        hash *= FNVPrime;
    }

    console.log(`[hash] ${key.toString()} ${hash} ${hash.toString(16)} ${hash % this.entries.length}`);
    return parseInt(hash % this.entries.length);
}
handlingCollision(key, hash, bool)
{
let newHash;
for(let i = 0; i < this.entries.length; i++)
{
newHash = (hash + i) % this.entries.length;
if (bool && (this.entries[newHash] || this.entries[newHash]._key != key))
{
return newHash;
}
else if (!bool && this.entries._key == key){
return newHash
}
}
return -1;
}
addToEntries(key, value)
{
let hash = this.getHash(key);
if(this.entries[hash] != null && this.entries[hash]._key != key){
hash = this.handlingCollision(key,value,true);
}
 if(hash = -1)
{
return new expect("wrong")
}
if(this.entries[hash] == null)
{
    let newpair = new KeyValuePair(key, value);
    this.entries[hash] = newpair;
}
if(this.entries[hash]._key == key)
{
    this.entries._value = value;
}
else {
    return new expect("wrong 2");
}
}
}
let table = new hashTable()
table.print()
table.set("Sinar", "sinar@gmail.com")
table.set("Elvis", "elvis@gmail.com")
table.set("Tane", "tane@gmail.com")
table.print()
console.log("[get] " + table.get("Sinar"))
table.set("Gerti", "gerti@gmail.com")
table.set("Arist", "arist@gmail.com")
table.print()
console.log("[get] " + table.get("Sinar"))
