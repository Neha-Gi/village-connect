print("# Village Connect - Core Models Implementation")
print("===========================================\n")

print("Below are the key Django models for the Village Connect application:\n")

print("## User and Profile Models")
print("```python")
print("""from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('regular', _('Regular User')),
        ('shop_owner', _('Shop Owner')),
        ('delivery', _('Delivery Person')),
        ('admin', _('Administrator')),
        ('diaspora', _('Diaspora Sender')),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='regular')
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    preferred_language = models.CharField(
        max_length=10, 
        choices=(
            ('en', _('English')),
            ('ha', _('Hausa')),
            ('yo', _('Yoruba')),
            ('ig', _('Igbo')),
            ('fr', _('French')),
        ),
        default='en'
    )
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    lga = models.CharField(max_length=100, null=True, blank=True)  # Local Government Area
    community = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class BusinessVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_verification')
    cac_certificate = models.FileField(upload_to='verification/cac/', null=True, blank=True)
    rc_number = models.CharField(max_length=50, null=True, blank=True)
    tin = models.CharField(max_length=50, null=True, blank=True)
    verification_status = models.CharField(
        max_length=20,
        choices=(
            ('pending', _('Pending')),
            ('approved', _('Approved')),
            ('rejected', _('Rejected')),
        ),
        default='pending'
    )
    verification_notes = models.TextField(null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Business Verification"
""")
print("```\n")

print("## Marketplace Models")
print("```python")
print("""from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=200)  # Where the product is located
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.product.name}"

class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('pending', _('Pending')),
        ('paid', _('Paid')),
        ('processing', _('Processing')),
        ('shipped', _('Shipped')),
        ('delivered', _('Delivered')),
        ('cancelled', _('Cancelled')),
    )
    
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    shipping_address = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Order #{self.id} by {self.buyer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at time of purchase
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
""")
print("```\n")

print("## Wallet and Payment Models")
print("```python")
print("""from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username}'s Wallet (₦{self.balance})"

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('deposit', _('Deposit')),
        ('withdrawal', _('Withdrawal')),
        ('payment', _('Payment')),
        ('refund', _('Refund')),
        ('commission', _('Commission')),
    )
    
    TRANSACTION_STATUS_CHOICES = (
        ('pending', _('Pending')),
        ('completed', _('Completed')),
        ('failed', _('Failed')),
        ('cancelled', _('Cancelled')),
    )
    
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=TRANSACTION_STATUS_CHOICES, default='pending')
    reference = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    related_order = models.ForeignKey('marketplace.Order', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.transaction_type} of ₦{self.amount} - {self.status}"

class Escrow(models.Model):
    order = models.OneToOneField('marketplace.Order', on_delete=models.CASCADE, related_name='escrow')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='buyer_escrows')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='seller_escrows')
    created_at = models.DateTimeField(auto_now_add=True)
    released_at = models.DateTimeField(null=True, blank=True)
    is_released = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Escrow for Order #{self.order.id} - ₦{self.amount}"
""")
print("```\n")

print("## Delivery and Pickup Models")
print("```python")
print("""from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import uuid

class PickupShop(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pickup_shops')
    name = models.CharField(max_length=200)
    address = models.TextField()
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)  # Local Government Area
    community = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)  # Percentage
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Delivery(models.Model):
    DELIVERY_STATUS_CHOICES = (
        ('pending', _('Pending')),
        ('in_transit', _('In Transit')),
        ('at_pickup_shop', _('At Pickup Shop')),
        ('delivered', _('Delivered')),
        ('cancelled', _('Cancelled')),
    )
    
    order = models.OneToOneField('marketplace.Order', on_delete=models.CASCADE, related_name='delivery')
    delivery_person = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='deliveries'
    )
    pickup_shop = models.ForeignKey(
        PickupShop, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='deliveries'
    )
    status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='pending')
    tracking_code = models.CharField(max_length=20, unique=True)
    qr_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    estimated_delivery_date = models.DateField(null=True, blank=True)
    actual_delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Delivery for Order #{self.order.id} - {self.get_status_display()}"
    
    class Meta:
        verbose_name_plural = 'Deliveries'

class DeliveryConfirmation(models.Model):
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE, related_name='confirmation')
    confirmed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    confirmed_at = models.DateTimeField(auto_now_add=True)
    confirmation_method = models.CharField(
        max_length=20,
        choices=(
            ('qr_code', _('QR Code')),
            ('otp', _('OTP')),
            ('admin', _('Admin Override')),
        )
    )
    confirmation_notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Confirmation for Delivery #{self.delivery.id}"

class DeliveryTracking(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='tracking_updates')
    status = models.CharField(max_length=20, choices=Delivery.DELIVERY_STATUS_CHOICES)
    location = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Update for Delivery #{self.delivery.id}: {self.get_status_display()}"
""")
print("```\n")

print("## Messaging Models")
print("```python")
print("""from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    related_order = models.ForeignKey('marketplace.Order', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Conversation #{self.id}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    original_language = models.CharField(max_length=10, default='en')
    
    def __str__(self):
        return f"Message from {self.sender.username} in Conversation #{self.conversation.id}"

class MessageAttachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='message_attachments/')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Attachment for Message #{self.message.id}"

class MessageTranslation(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10)
    translated_content = models.TextField()
    
    class Meta:
        unique_together = ('message', 'language')
    
    def __str__(self):
        return f"Translation of Message #{self.message.id} to {self.language}"
""")
print("```\n")

print("## Report and Admin Models")
print("```python")
print("""from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Report(models.Model):
    REPORT_TYPE_CHOICES = (
        ('user', _('User')),
        ('product', _('Product')),
        ('message', _('Message')),
        ('delivery', _('Delivery')),
        ('other', _('Other')),
    )
    
    REPORT_STATUS_CHOICES = (
        ('pending', _('Pending')),
        ('investigating', _('Investigating')),
        ('resolved', _('Resolved')),
        ('dismissed', _('Dismissed')),
    )
    
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports_filed')
    reported_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='reports_against'
    )
    reported_product = models.ForeignKey(
        'marketplace.Product', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    reported_message = models.ForeignKey(
        'messaging.Message', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=REPORT_STATUS_CHOICES, default='pending')
    resolved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='resolved_reports'
    )
    resolution_notes = models.TextField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Report #{self.id} - {self.get_report_type_display()}"

class AdminLog(models.Model):
    admin_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_logs')
    action = models.CharField(max_length=255)
    model_affected = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.admin_user.username} - {self.action} - {self.timestamp}"

class BlockedUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='block_status')
    blocked_at = models.DateTimeField(auto_now_add=True)
    blocked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='users_blocked'
    )
    reason = models.TextField()
    is_permanent = models.BooleanField(default=False)
    unblock_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Blocked: {self.user.username}"
""")
print("```\n")

print("These models provide the foundation for the Village Connect application, covering all the key features mentioned in the requirements. The models are organized into logical groups and include relationships between them to support the application's functionality.")
