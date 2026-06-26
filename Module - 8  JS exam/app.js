
// product_load
const loadallProduct = () => {
    fetch("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=vodka")
        .then((res) => res.json())
        .then((data) => {
                displayProduct(data.drinks); 
                console.log(data);
        })
};

// disply_product
const displayProduct = (products) => {
    const product_container = document.getElementById("product-container");
    // if product not found
    product_container.innerHTML = ""; 
    if (!products) {
        product_container.innerHTML = `
                <h3 style="color: red;">No drinks found! Please try another name.</h3>
        `;
        return;
    }
    // display product inner HTML
    products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("product-card");
        div.innerHTML = `
        <img src="${product.strDrinkThumb}" alt="${product.strDrink}" style="width:100%; max-width:200px;"/>
        <h4><strong>Name : </strong>${product.strDrink}</h4><hr>
        <p><strong>Category : </strong>${product.strCategory}</p>
        <p><strong>Glass : </strong>${product.strGlass}</p>
        <p><strong>Instraction : </strong>${product.strInstructions.slice(0,15)}</p>
        <button onclick="singleProduct('${product.idDrink}')"> Details </button>
        <button onclick="add_to_group('${product.strDrink}','${product.strCategory}')"> Add to Group </button>
        `;
        product_container.appendChild(div);
    });
};

// add to cart
const add_to_group = (name,category) => {
    const cartCount = document.getElementById("count").innerText;
    let convaert = parseInt(cartCount);
    // cannot add more than 7 drinks
    if (convaert >= 7) {
        alert("You cannot add more than 7 drinks!");
        return;
    }
    convaert += 1;
    document.getElementById("count").innerText = convaert;
    const container = document.getElementById("cart-main-container");
    const div = document.createElement("div");
    div.classList.add("DIV");

    // cart showing details
    div.innerHTML = `<h3>${name}</h3> 
    <p>-${category}</p>
    `;
    container.appendChild(div);
};


// products details or details button click
const singleProduct = (id) => {
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((res) => res.json())
    .then((data) => {
        const product = data.drinks[0];
        const modalBody = document.getElementById("modal-body");
        modalBody.innerHTML = `
            <h2>${product.strDrink}</h2>
            <img src="${product.strDrinkThumb}" style="width: 100%; max-width: 180px; border-radius: 8px;" />
            <p><strong>Category:</strong> ${product.strCategory}</p>
            <p><strong>Type:</strong> ${product.strAlcoholic}</p>
            <p><strong>Glass : </strong>${product.strGlass}</p>
            <p><strong>Description: </strong>${product.strInstructions}</p>
            <button class="close-btn" onclick="closeModal()">Close</button>
        `;
        document.getElementById("product-modal").style.display = "flex";
    }); 
};

const closeModal = () => {
    document.getElementById("product-modal").style.display = "none";
};

//  search products
const searchProduct = () => {
    const search_item = document.getElementById("search-input").value;

    if (search_item === "") {
        alert("Enter search item!");
        loadallProduct();
        return;
    }

    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${search_item}`)
        .then((res) => res.json())
        .then((data) => {
            displayProduct(data.drinks);
        })
};


loadallProduct();