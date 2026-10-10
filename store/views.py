from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Order, OrderItem

def register(r):
    form = UserCreationForm(r.POST or None)
    if form.is_valid():
        login(r, form.save()); return redirect("home")
    return render(r, "registration/register.html", {"form": form})

def product_list(r):
    q, cat, sort = r.GET.get("q", ""), r.GET.get("cat", ""), r.GET.get("sort", "")
    ps = Product.objects.filter(name__icontains=q)
    if cat: ps = ps.filter(category=cat)
    ps = ps.order_by({"low": "price", "high": "-price", "top": "-rating"}.get(sort, "id"))
    cats = Product.objects.values_list("category", flat=True).distinct().order_by("category")
    return render(r, "store/list.html", {"products": ps, "q": q, "cat": cat, "cats": cats, "sort": sort})

def product_detail(r, pk):
    p = get_object_or_404(Product, pk=pk)
    return render(r, "store/detail.html", {"p": p, "related": Product.objects.filter(category=p.category).exclude(pk=pk)[:4]})

def _cart(r):
    items, total = [], Decimal(0)
    for pid, qty in r.session.get("cart", {}).items():
        p = Product.objects.filter(pk=pid).first()
        if p:
            items.append({"p": p, "qty": qty, "sub": p.price * qty}); total += p.price * qty
    return items, total

def cart_view(r):
    items, total = _cart(r)
    return render(r, "store/cart.html", {"items": items, "total": total})

def _change(r, pk, delta):
    c = r.session.get("cart", {}); n = c.get(str(pk), 0) + delta
    if n > 0: c[str(pk)] = n
    else: c.pop(str(pk), None)
    r.session["cart"] = c
    return redirect(r.META.get("HTTP_REFERER") or "cart")

def cart_add(r, pk): return _change(r, pk, 1)
def cart_dec(r, pk): return _change(r, pk, -1)
def cart_remove(r, pk): return _change(r, pk, -99)

@login_required
def checkout(r):
    items, total = _cart(r)
    if r.method == "POST" and items:
        o = Order.objects.create(user=r.user, total=total, address=r.POST.get("address", ""))
        for i in items: OrderItem.objects.create(order=o, product=i["p"], qty=i["qty"], price=i["p"].price)
        r.session["cart"] = {}
        return redirect("orders")
    return redirect("cart")

@login_required
def orders(r):
    return render(r, "store/orders.html", {"orders": Order.objects.filter(user=r.user).order_by("-created")})
