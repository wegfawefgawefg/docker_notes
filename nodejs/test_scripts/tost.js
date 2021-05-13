function allEqual(arr) {
    let first = arr[0];
    for(let i = 1; i < arr.length; i++)
    {
        let another = arr[i];
        if(!(first === another)){
            return false;
       }
    }
    return true;
}

e = [1, 1, 1, 1];
ne = [1, 2, 3, 5];
console.log(allEqual(e));
console.log(allEqual(ne));