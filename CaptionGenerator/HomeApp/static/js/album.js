  function _upload(){
    $.ajax({
      method:'get',
      url:'/login/sessioncheck/',
      data:{},
      success:function(e){
        console.log(e.Result)
        if (e.Result){
        document.getElementById('file_upload_id').click();
      }
      else{
        $('#message').html('Please Login To Continue');
        $('#message').css('color','red');
        console.log('login required')
      }
      },
      error:function(e){
      }
    
})
}

  function readURL(input) {
  
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#upload_ImageId').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#file_upload_id").change(function() {
  readURL(this);
});

function imagecheck(){
  if ($('#file_upload_id').val()){
    $('#caption-form').submit();
  }
  else{
    alert('Please Select Image First');
  }
}