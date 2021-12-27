$(document).ready(function(){
    //login form validation
      $("#signup-form").validate({
          rules:{
             
               module: { required: true },
            
            username:{
                required: true,
                minlength: 3
            },
            password:{
                required: true,
                minlength: 8
            }
          },
          messages:{
            module: {required: "Please select your role!" },
            username:{
                required: "please enter your username",
                minlength: "please enter username of min 3 charecters"
            },
            password:{
                required: "please enter your password",
                minlength: "enter password of min 8 charecters"
            }
          }
      }),
    
      //doctor validation
      $("#doctor-form").validate({
        rules:{
           
             fname:"required",
             lname:"required",
          
          age:{
              required: true,
              maxlength: 2
          },
          mobile:{
              required:true,
              number: true,
              minlength: 10,
              maxlength: 10
          },
          password:{
              required: true,
              minlength: 8
          },
          place:"required",
          email:{
            required: true,
            email:true
          },
          quali:{
              required:true
          },
          dep:{
              required:true
          },
          date:"required",
          exp:"required",
          address:{
              required:true,
              minlength:3
          },
          inputimage:{
            required: true,
             extension: "png|jpeg|gif",
              filesize: 1048576 
          },
          description:"required",
          
        },
        messages:{
          fname:"* please enter your firstname",
          lname:"* please enter your lastname",
          age:{
              required: "* please enter your age",
              minlength: "* please enter a valid age"
          },
          mobile:{
            required:"* Mobile Number Required",
            number:"Enter Valid Mobile Number",
            minlength: "Enter Valid Mobile Number",
            maxlength: "Enter Valid Mobile Number"
        },
       

          password:{
              required: "* please enter your password",
              minlength: "* enter password of min 8 charecters"
          },
          place:"* please enter your place",

          email:{
              required:"* please enter your email",
              email:"* please enter a valid email address"
          },
          quali:{
              required:"* please select your qualification"
          },
          dep:{
              required:"* Please select your department"
          },
          date:"* please Enter your Join Date",
          exp:"* please enter your Experience",
          address:{
            required:"* please enter your Address",
            minlength:"* please enter address of min 2 charecters "
        },
        inputimage:
        {
            required:"* upload image of type jpeg,png or gif lessthan 1 MB"
        },
        description:"* please enter doctor description",
        }
    }),
    //appointment form validation
    
    $("#appoint-form").validate({
        rules:{
           
             fname:"required",
             lname:"required",
          
          age:{
              required: true,
              maxlength: 2
          },
          mobile:{
              required:true,
              number: true,
              minlength: 10,
              maxlength: 10
          },
         
          doc:{
              required:true
          },
          dep:{
              required:true
          },
          address:{
              required:true,
              minlength:3
          }
        },
        messages:{
          fname:"* please enter your firstname",
          lname:"* please enter your lastname",
          age:{
              required: "* please enter your age",
              minlength: "* please enter a valid age"
          },
          mobile:{
            required:"Mobile Number Rquired",
            number:"Enter Valid Mobile Number",
            minlength: "Enter Valid Mobile Number",
            maxlength: "Enter Valid Mobile Number"
        },
        doc:"* please select your doctor",
        dep:"* please select your department",
        
          address:{
            required:"* please enter your Address",
            minlength:"* please enter address of min 2 charecters "
        }
        }
    }),
    //department validation
    
    $("#dep-form").validate({
        rules:{
           
            dep:"required",
    
            inputimage: {
                required: true,
                extension: "png|jpe?g|gif",
                filesize: 1048576  },
           
            description:{
              required:true,
              minlength:20
          }
        },
        messages:{
          dep:"* please enter department",
          inputimage: "*File must be JPG, GIF or PNG, less than 1MB",
         
          description:{
            required:"* please enter your Address",
            minlength:"* please enter address of min 20 charecters "
        }
        }
    })
    
    
    
    })
    
    
    $(document).ready(function(){
        $(window).resize(function() {
            if ($(window).width() <= 768) 
            {
                console.log("hi")
                $("#navshow").hide();
                
                $(".button-class").click(function(){
                $("#navshow").toggle()
       
                 })
            }  
        else {
            $("#navshow").show();
        }
            });
    
            if ($(window).width() <= 768) 
            {
                $(".button-class").click(function(){
                $("#navshow").toggle()
       
                 })
            } 
          
            });
    
            $(document).ready(function(){
                $("#dep-search").on("keyup", function() {
                    
                  var value = $(this).val().toLowerCase();
                  $("#doctor-table tr").filter(function() {
                    $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
                  });
                  $("#docappointment tr").filter(function() {
                    $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
                  });
                });
              });
       
       
    
      
      
      