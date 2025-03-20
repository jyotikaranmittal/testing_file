console.log('Hello, World!');
console.log("electricvehicles");

function getting_data() {
    fetch("/EVP")
        .then(response => response.json())
    
        
        .then(data => {
            console.log(data);
            
        });
}



