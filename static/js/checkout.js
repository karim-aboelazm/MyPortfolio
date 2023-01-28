$(document).ready(function (){
    $('.PayWithRazor').click(function(e){
        e.preventDefault();
        var first_name     = $("[name='first_name']").val();
        var last_name      = $("[name='last_name']").val();
        var email_address  = $("[name='email']").val();
        var phone_number   = $("[name='phone_num']").val();
        var token          = $("[name='csrfmiddlewaretoken']").val();
        if(first_name == "" || last_name == "" || email_address == "" || phone_number == ""){
            swal("alart!", "All Fields Are Mandatory!", "error");
            return false;
        }
        else{
            $.ajax({
                method : "GET",
                url : "/proceed-to-pay",
                success: function (response){
                    // console.log(response);
                    var options = {
                        "key": "YOUR_KEY_ID", // Enter the Key ID generated from the Dashboard
                        "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Acme Corp",
                        "description": "Test Transaction",
                        "image": "https://example.com/your_logo",
                        "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (response){
                            data = {
                                "first_name" : first_name   ,   
                                "last_name" : last_name    ,    
                                "email_address" : email_address,
                                "phone_number" : phone_number , 
                                "payment_mode":"paid by Paypal", 
                                csrfmiddlewaretoken : token,
                            }
                            $.ajax({
                                method: "POST",
                                url:"/check-out",
                                data:data,
                                dataType : "dataType",
                                success : function (response){

                                }

                            });
                        },
                        
                        
                        
                        "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",
                        "prefill": {
                            "name": "Gaurav Kumar",
                            "email": "gaurav.kumar@example.com",
                            "contact": "9000090000"
                        },
                        "notes": {
                            "address": "Razorpay Corporate Office"
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                }
            });
            
            
        }

       
    });
});