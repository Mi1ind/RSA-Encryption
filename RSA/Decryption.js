/* Need to recreate Decryption.py with java script,
so it can be run directly from the google database 

Sheets and python implementation:
https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
*/


txt = 59382905295494935044184712745115080192043246656878300358332659046924207232136798080076617067660730664412827240773628056844786186400672539523293533955668238614064246108862474415544109400020356984223118364638044287266897557588278807127000266323981797875452877180764975183405975548607370132548400015448326116755n
modulus = 145906768007583323230186939349070635292401872375357164399581871019873438799005358938369571402670149802121818086292467422828157022922076746906543401224889672472407926969987100581290103199317858753663710862357656510507883714297115637342788911463535102712032765166518411726859837988672111837205085526346618740053n
exponent = 89489425009274444368228545921773093919669586065884257445497854456487674839629818390934941973262879616797970608917283679875499331574161113854088813275488110588247193077582527278437906504015680623423550067240042466665654232383502922215493623289472138866445818789127946123407807725702626644091036502372545139713n

// Algorithm which calculates base^exponent % modulus
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


function numToStr(asciiNum) {
    // Makes every digit an element of the array lst
    var lst = Array.from(String(asciiNum), Number)
    lst.push('*');
    answer = '';
    finalLst = [];

    // Create nested arrays then used arratName.join() function.
    while (lst[0] != '*') {
        if (lst[0] == 1) {
            finalLst.push(lst.splice(0, 3).join(''));
        }
        else {
            finalLst.push(lst.splice(0, 2).join(''));
        }
    }

    for (i = 0; i < finalLst.length; i++) {
        answer += String.fromCharCode(finalLst[i]);

    }
    return answer;

}



console.log(numToStr(72105321091213211097109101321051153277105108105110100n))

