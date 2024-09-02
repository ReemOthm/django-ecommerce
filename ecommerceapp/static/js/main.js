function totalPrice(price){
    qty = document.getElementById("product_qty").value 
    total = document.getElementById("total-price") 
    total.textContent = price * qty
}