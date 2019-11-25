/* Need to recreate Decryption.py with java script,
so it can be run directly from the google database 

Sheets and python implementation:
https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
*/

/*function numToStr(self, asciiNum) {

}
function decAnswer(self) {

}*/

txt = 49753325574865445089772669052891000483752580109613466912771010336607847769281978866460532307952123513083663621765806989683259320224009128424843195798482983529142744938925210736045258659747179875853414003793568639616690520031318358365189672329709227585258829062097623252983992310067500221135568184405349569803n
modulus = 145906768007583323230186939349070635292401872375357164399581871019873438799005358938369571402670149802121818086292467422828157022922076746906543401224889672472407926969987100581290103199317858753663710862357656510507883714297115637342788911463535102712032765166518411726859837988672111837205085526346618740053n
exponent = 89489425009274444368228545921773093919669586065884257445497854456487674839629818390934941973262879616797970608917283679875499331574161113854088813275488110588247193077582527278437906504015680623423550067240042466665654232383502922215493623289472138866445818789127946123407807725702626644091036502372545139713n

// calculates   base^exponent % modulus
function powerMod(base, exponent, modulus) {
    if (modulus === 1n) return 0;
    var result = 1n;
    base = base % modulus;
    while (exponent > 0n) {
        if (exponent % 2n === 1n)  //odd number
            result = (result * base) % modulus;
        exponent = exponent >> 1n; //divide by 2
        base = (base * base) % modulus;
    }
    return result;
}

// console.log(powerMod(txt, exponent, modulus))


function numToStr(asciiNum) {
    var lst = Array.from(String(asciiNum), Number)
    lst.push('*');
    answer = '';

    finalLst = [];
    j = 0;
    a = ''

    while (lst[j] != '*') {
        if (lst[j] == 1) {
            finalLst.push(a.join(lst[j]))
            j += 3
        }
        else {
            finalLst.push(a.join(lst[j]))
            j += 2
        }
        // console.log(lst[j])
    }

    return lst;

}

console.log(numToStr(65656565))













