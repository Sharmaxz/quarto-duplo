from hotelshare.models import user, request, hotel, event, match, local

user.User.register_admin()
request.Request.register_admin()
hotel.Hotel.register_admin()
event.Event.register_admin()
match.Match.register_admin()
local.Local.register_admin()
