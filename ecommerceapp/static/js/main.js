function totalPrice(price){
    qty = document.getElementById("product_qty").value 
    total = document.getElementById("total-price") 
    total.textContent = price * qty
}

function addToCart(id){
    const cartIcon = document.getElementById("cart-icon")
    const ajaxUrl = '/add_to_cart/'
    
    $.ajax({
        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url: ajaxUrl,
        data:{id:id},
        method:"post",
        success: function(response){
            cartIcon.textContent = response.count
            Swal.fire({
                position: "top-end",
                icon: "success",
                width: "350px",
                title: "تم إضافة المنتج الى السلة",
                showConfirmButton: false,
                timer: 1500
            })
        }
    });
}

function deleteItemFromCart(id){
    const cartIcon = document.getElementById("cart-icon")
    const ajaxUrl = '/delete_item_from_cart/'

    $.ajax({
        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url: ajaxUrl,
        data:{id:id},
        method:"post",
        success: function(response){
            cartIcon.textContent = response.count
            location.reload()
        }
    });
}
