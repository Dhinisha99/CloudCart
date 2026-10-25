from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CloudCart | Smart Shopping</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #1e293b;
        }

        header {
            background: #111827;
            color: white;
            padding: 22px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }

        .logo {
            font-size: 28px;
            font-weight: bold;
        }

        .logo span {
            color: #38bdf8;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 24px;
            font-size: 15px;
        }

        .hero {
            padding: 75px 8%;
            background: linear-gradient(120deg, #0f172a, #1d4ed8);
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 35px;
            flex-wrap: wrap;
        }

        .hero-content {
            max-width: 580px;
        }

        .hero h1 {
            font-size: clamp(36px, 5vw, 58px);
            line-height: 1.15;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 18px;
            line-height: 1.7;
            color: #dbeafe;
            margin-bottom: 28px;
        }

        .button {
            display: inline-block;
            background: #38bdf8;
            color: #082f49;
            padding: 14px 25px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        }

        .hero-card {
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
            padding: 35px;
            border-radius: 20px;
            text-align: center;
            min-width: 230px;
        }

        .hero-card .icon {
            font-size: 85px;
            margin-bottom: 15px;
        }

        .hero-card h2 {
            font-size: 22px;
            margin-bottom: 10px;
        }

        .section {
            padding: 60px 8%;
        }

        .section-heading {
            text-align: center;
            margin-bottom: 35px;
        }

        .section-heading h2 {
            font-size: 34px;
            margin-bottom: 12px;
        }

        .section-heading p {
            color: #64748b;
        }

        .products {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 25px;
        }

        .product {
            background: white;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(15, 23, 42, 0.06);
            transition: transform 0.2s;
        }

        .product:hover {
            transform: translateY(-5px);
        }

        .product-icon {
            font-size: 65px;
            padding: 20px;
            margin-bottom: 15px;
            background: #eff6ff;
            border-radius: 12px;
        }

        .product h3 {
            margin-bottom: 10px;
        }

        .product p {
            color: #64748b;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 15px;
        }

        .price {
            color: #2563eb;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 18px;
        }

        .buy-button {
            display: inline-block;
            padding: 11px 20px;
            background: #2563eb;
            color: white;
            border-radius: 7px;
            text-decoration: none;
        }

        .features {
            background: white;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 25px;
            padding: 40px 8%;
            text-align: center;
        }

        .feature h3 {
            margin: 12px 0;
        }

        .feature p {
            color: #64748b;
            font-size: 14px;
        }

        footer {
            background: #111827;
            color: #cbd5e1;
            text-align: center;
            padding: 25px;
            line-height: 1.8;
        }

        @media (max-width: 600px) {
            header {
                padding: 20px 5%;
            }

            nav a {
                margin-left: 0;
                margin-right: 15px;
            }

            .hero, .section {
                padding: 45px 5%;
            }

            .hero-card {
                width: 100%;
            }
        }
    </style>
</head>

<body>

<header>
    <div class="logo">Cloud<span>Cart</span></div>

    <nav>
        <a href="/">Home</a>
        <a href="#products">Products</a>
        <a href="#features">Why CloudCart?</a>
    </nav>
</header>

<section class="hero">
    <div class="hero-content">
        <h1>Smart Shopping.<br>Smarter Living.</h1>

        <p>
            Discover quality products, explore new arrivals,
            and enjoy a simple shopping experience with CloudCart.
        </p>

        <a href="#products" class="button">Explore Products →</a>
    </div>

    <div class="hero-card">
        <div class="icon">🛍️</div>
        <h2>Your Shopping Destination</h2>
        <p>Simple. Modern. Convenient.</p>
    </div>
</section>

<section class="section" id="products">
    <div class="section-heading">
        <h2>Featured Products</h2>
        <p>Explore our popular product collection.</p>
    </div>

    <div class="products">
        <div class="product">
            <div class="product-icon">🎧</div>
            <h3>Wireless Headphones</h3>
            <p>Enjoy your favorite music with a modern wireless design.</p>
            <div class="price">₹1,499</div>
            <a href="#features" class="buy-button">Explore</a>
        </div>

        <div class="product">
            <div class="product-icon">⌚</div>
            <h3>Smart Watch</h3>
            <p>A stylish accessory for your everyday activities.</p>
            <div class="price">₹2,499</div>
            <a href="#features" class="buy-button">Explore</a>
        </div>

        <div class="product">
            <div class="product-icon">🎒</div>
            <h3>Travel Backpack</h3>
            <p>A practical companion for work, travel, and daily use.</p>
            <div class="price">₹999</div>
            <a href="#features" class="buy-button">Explore</a>
        </div>

        <div class="product">
            <div class="product-icon">📱</div>
            <h3>Mobile Accessories</h3>
            <p>Discover useful accessories for your everyday devices.</p>
            <div class="price">₹599</div>
            <a href="#features" class="buy-button">Explore</a>
        </div>
    </div>
</section>

<section class="features" id="features">
    <div class="feature">
        <div style="font-size: 38px;">🚚</div>
        <h3>Convenient Shopping</h3>
        <p>Browse products from one simple website.</p>
    </div>

    <div class="feature">
        <div style="font-size: 38px;">🔒</div>
        <h3>Security Focused</h3>
        <p>Built as a foundation for secure application development.</p>
    </div>

    <div class="feature">
        <div style="font-size: 38px;">☁️</div>
        <h3>Cloud Ready</h3>
        <p>Designed as the starting point for a cloud deployment project.</p>
    </div>
</section>

<footer>
    <h3>CloudCart — Smart Shopping Experience</h3>
    <p>Python Flask | AWS DevOps Capstone Project</p>
    <p>© 2026 CloudCart. Educational project.</p>
</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/health")
def health():
    return {"status": "healthy", "application": "CloudCart"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)