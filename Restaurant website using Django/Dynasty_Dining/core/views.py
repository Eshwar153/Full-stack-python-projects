from django.shortcuts import render,redirect
# from django.contrib import messages
from .forms import FeedbackForm
from .forms import BookingForm
from .models import Booking
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
# from xhtml2pdf import pisa
from django.db import connection
# from .models import Order
from django.utils import timezone
from .models import FoodOrder
from .models import CouponSubmission 
from .forms import CouponForm 
from .models import Booking,Payment
from xhtml2pdf import pisa
from .utils import render_to_pdf



def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def archive(request):
    return render(request, 'core/Archive.html')

def booking(request):
    return render(request, 'core/booking.html')

def contact(request):
    return render(request, 'core/contact.html')

def feature(request):
    return render(request, 'core/feature.html')

def menu(request):
    return render(request, 'core/menu.html')

# def order_now(request):
#     return render(request, 'core/Order now.html')

def popup(request):
    return render(request, 'core/pop up.html')

def popup2(request):
    return render(request, 'core/Popup.html')

def read_more(request):
    return render(request, 'core/Read more-1.html')

def team(request):
    return render(request, 'core/team.html')

def offers(request):
    return render(request, 'core/offers.html')

def user_info(request):
    coupon_code = request.GET.get('code', '')
    offer_name = request.GET.get('offer', '')

    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            submission = form.save()
            return redirect('coupon_proof', submission_id=submission.id)
    else:
        form = CouponForm(initial={'coupon_code': coupon_code, 'offer_name': offer_name})

    return render(request, 'core/user_info.html', {'form': form})
    
def coupon_proof(request, submission_id):
    submission = CouponSubmission.objects.get(id=submission_id)
    return render(request, 'core/coupon_proof.html', {'submission': submission})


def coupon_success(request):
    return render(request, 'core/coupon_success.html')

# def user_info(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         coupon = request.POST.get('coupon')
#         offer = request.POST.get('offer')  # Passed as hidden input

#         # Store or process data here...

#         # Redirect to success page with offer info
#         return redirect('coupon_success', offer=offer)

#     offer = request.GET.get('offer', '')
#     code = request.GET.get('code', '')
#     return render(request, 'user_info.html', {'offer': offer, 'code': code})

def submit_user_info(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        coupon = request.POST.get('coupon')

        # Redirect to a page that displays the coupon info
        return redirect('coupon_success', full_name=full_name, email=email, coupon=coupon)
    
    # def CouponSubmission(request):
    #  offer_name = request.GET.get('offer')
    # coupon_code = request.GET.get('code')

    # if request.method == 'POST':
    #     full_name = request.POST.get('full_name')
    #     email = request.POST.get('email')
    #     entered_coupon = request.POST.get('coupon_code')

    #     # You can now render a coupon proof template
    #     return render(request, 'coupon_proof.html', {
    #          'offer_name': offer_name,
    #         'full_name': full_name,
    #         'email': email,
    #         'coupon_code': entered_coupon,
    #     })

    # return render(request, 'user_info.html', {
    #     'offer_name': offer_name,
    #     'coupon_code': coupon_code,
    # }) 

# def CouponSubmission(request):
#     # These come from the URL: ?offer=...&code=...
#     offer_name = request.GET.get('offer', '')
#     coupon_code = request.GET.get('code', '')

#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         entered_coupon = request.POST.get('coupon_code')  # From the form

#         return render(request, 'core/coupon_proof.html', {
#             'offer_name': offer_name,
#             'full_name': full_name,
#             'email': email,
#             'coupon_code': entered_coupon,
#         })

  # # Initial page load (form)
    # return render(request, 'core/user_info.html', {
    #     'offer_name': offer_name,
    #     'coupon_code': coupon_code,
    # })

def submit_coupon(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        coupon_code = request.POST.get('coupon_code')
        offer_name = request.POST.get('offer_name')

        # Save to DB
        CouponSubmission.objects.create(
            full_name=name,
            email=email,
            coupon_code=coupon_code,
            offer_name=offer_name
        )

        # Save to session to pass to the proof page
        request.session['name'] = name
        request.session['email'] = email
        request.session['coupon_code'] = coupon_code
        request.session['offer_name'] = offer_name

        return redirect('coupon_proof')

    # ✅ Always return something for GET requests too
    return render(request, 'core/user_info.html')

def offer_page(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            coupon_submission = form.save()

            # Redirect to the coupon success page after submission
            return redirect('coupon_success', pk=coupon_submission.pk)
    else:
        form = CouponForm()
    return render(request, 'core/offer_page.html', {'form': form})


    
# def coupon_proof(request, submission_id):
#     submission = CouponSubmission.objects.get(id=submission_id)
#     return render(request, 'core/coupon_proof.html', {'submission': submission})

# def coupon_success(request):
#     full_name = request.GET.get('full_name')
#     email = request.GET.get('email')
#     coupon = request.GET.get('coupon')
#     return render(request, 'core/coupon_success.html', {
#         'full_name': full_name,
#         'email': email,
#         'coupon': coupon
#     })

def privacy_policy(request):
    return render(request, 'core/privacy policy.html')

def FAQ(request):
    return render(request, 'core/FAQ.html')

def terms_of_use(request):
    return render(request, 'core/terms_of_use.html')

def help(request):
    return render(request, 'core/help.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/feedback_thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'core/feedback_form.html', {'form': form})





def food_order(request):
    return render(request, 'core/food_order.html') 



def process_order(request):
    if request.method == 'POST':
        name = request.POST.get('dish_name')
        price = float(request.POST.get('dish_price', 0))
        quantity = int(request.POST.get('quantity'))
        total = price * quantity

        # Save order to database
        order = FoodOrder.objects.create(
            dish_name=name,
            price=price,
            quantity=quantity,
            total=total
        )

        return redirect('receipt', order_id=order.id)
    return redirect('index')

def order_success(request):
    return render(request, 'order_success.html')

# views.py
# def order_receipt(request, order_id):
#     order = FoodOrder.objects.get(id=order_id)
#     return render(request, 'core/receipt.html', {'order': order})

def receipt(request, order_id):
    order = FoodOrder.objects.get(id=order_id)
    return render(request, 'core/receipt.html', {'order': order})


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_receipt', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'core/booking.html', {'form': form})

def booking_receipt_view(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'core/booking_receipt.html', {'booking': booking})

def payment_view(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        card_holder = request.POST.get('card_holder')
        card_number = request.POST.get('card_number')
        Payment.objects.create(
            booking=booking,
            card_holder=card_holder,
            card_number=card_number
        )
        return redirect('payment_receipt', booking_id=booking.id)
    return render(request, 'core/payment_page.html', {'booking': booking})

def payment_receipt_view(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    payment = Payment.objects.get(booking=booking)
    return render(request, 'core/payment_receipt.html', {'booking': booking, 'payment': payment})


def booking_pdf_view(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    pdf = render_to_pdf('core/booking_receipt.html', {'booking': booking})
    return HttpResponse(pdf, content_type='application/pdf')

def payment_pdf_view(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    payment = Payment.objects.get(booking=booking)
    pdf = render_to_pdf('core/payment_receipt.html', {'booking': booking, 'payment': payment})
    return HttpResponse(pdf, content_type='application/pdf')





# Create your views here.
