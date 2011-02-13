function CurrentDate()
	{
	 var currentTime = new Date();
	 var month       = currentTime.getMonth() + 1;
	 var day         = currentTime.getDate();
	 var year        = currentTime.getFullYear();
	 return (month + "/" + day + "/" + year);
	}
	function CurrentTime()
	{
	 var currentTime = new Date();
	 var hours       = currentTime.getHours();
	 var minutes     = currentTime.getMinutes();
	 if (minutes < 10)
	 {
	   minutes = "0" + minutes;
	 }
	 if(hours > 11)
	 {
	  if(hours == 12)
	  {
	   return ("12:" + minutes + " PM");
	  }
	  else
	  {
	   return ((hours - 12) + ":" + minutes + " PM");
	  }
	 }
	 else
	 {
	  if(hours == 0)
	  {
	   return ("12:" + minutes + " AM");
	  }
	  else
	  {
	   return ((hours) + ":" + minutes + " AM");
	  }
	 }
	}
	function CurrentDateTime()
	{
	 return (CurrentDate() + " " + CurrentTime());
	}
	