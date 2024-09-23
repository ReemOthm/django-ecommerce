const cartIcon = document.getElementById("cart-icon")

function totalPrice(price){
    qty = document.getElementById("product_qty").value
    total = document.getElementById("total-price") 
    total.textContent = price * qty
}

function addToCart(page,id, name, image, color, itemPrice){
    let qty,price;
    if(page == false){
        qty = document.getElementById("product_qty").value
        price = parseFloat(document.getElementById("total-price").textContent.trim())
    } else {
        qty = 1
        price = itemPrice
    }
    const ajaxUrl = '/add_to_cart/'
    $.ajax({
        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url: ajaxUrl,
        data:{id:id, name:name, image:image,color:color,qty:qty,price:price},
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

function changeQty(action,id){
    const ajaxUrl = '/change_qty/'
    const cartitemPrice = document.getElementById("cartitem-price"+id)
    $.ajax({
        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url: ajaxUrl,
        data:{action: action,id:id},
        method:"post",
        success: function(response){
            cartIcon.textContent = response.count;
            cartitemPrice.textContent = response.price;
            Swal.fire({
                position: "top-end",
                icon: "success",
                width: "350px",
                showConfirmButton: false,
                timer: 1500
            })
        }
    });
}

function deleteItemFromCart(id){
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

function removeAllItems(){
    const ajaxUrl = '/remove_all_items/'

    $.ajax({
        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url: ajaxUrl,
        data:{},
        method:"post",
        success: function(response){
            cartIcon.textContent = response.count
            location.reload()
        }
    });
}