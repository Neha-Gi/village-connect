import Image from "next/image"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { ArrowRight, ShoppingBag, Truck, Wallet, MessageCircle, Globe, Shield, Users } from "lucide-react"

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      <header className="bg-gradient-to-r from-green-600 to-green-800 text-white">
        <div className="container mx-auto px-4 py-16 md:py-24">
          <div className="flex flex-col md:flex-row items-center gap-8">
            <div className="flex-1 space-y-6">
              <h1 className="text-4xl md:text-6xl font-bold">Connecting Villages to the World</h1>
              <p className="text-xl md:text-2xl opacity-90">
                A secure marketplace and delivery network built for remote communities
              </p>
              <div className="flex flex-wrap gap-4">
                <Button size="lg" className="bg-white text-green-800 hover:bg-gray-100">
                  Get Started
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button size="lg" variant="outline" className="border-white text-white hover:bg-white/10">
                  Learn More
                </Button>
              </div>
            </div>
            <div className="flex-1">
              <Image
                src="/placeholder.svg?height=400&width=500"
                alt="Village Connect App"
                width={500}
                height={400}
                className="rounded-lg shadow-xl"
              />
            </div>
          </div>
        </div>
      </header>

      {/* Features Section */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">Main Features</h2>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <FeatureCard
              icon={<Users />}
              title="Create Your Account"
              description="Sign up with phone, email, or social media. Add your details and verify your business if needed."
            />
            <FeatureCard
              icon={<ShoppingBag />}
              title="Send & Receive Goods"
              description="Sell farm products to town buyers or order goods from the city with live tracking."
            />
            <FeatureCard
              icon={<Wallet />}
              title="Secure Digital Wallet"
              description="Load money, pay for items and delivery. All funds are held safely until delivery confirmation."
            />
            <FeatureCard
              icon={<Truck />}
              title="Local Pickup Shops"
              description="Village shopkeepers can register as pickup centers, earning commission for helping with deliveries."
            />
            <FeatureCard
              icon={<MessageCircle />}
              title="Messaging and Chat"
              description="Chat privately with sellers, buyers, or delivery drivers with admin oversight for security."
            />
            <FeatureCard
              icon={<Globe />}
              title="Multi-Language Support"
              description="Use the app in English, Hausa, Yoruba, Igbo, or French with auto-translation."
            />
          </div>
        </div>
      </section>

      {/* Security Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row items-center gap-12">
            <div className="flex-1">
              <Image
                src="/placeholder.svg?height=400&width=500"
                alt="Security Features"
                width={500}
                height={400}
                className="rounded-lg shadow-lg"
              />
            </div>
            <div className="flex-1 space-y-6">
              <h2 className="text-3xl md:text-4xl font-bold">Security You Can Trust</h2>
              <p className="text-lg text-gray-700">
                Our platform is built with multiple layers of protection to ensure safe transactions and secure
                communications.
              </p>
              <ul className="space-y-4">
                <SecurityFeature
                  title="Protected Payments"
                  description="All money is secured with escrow until delivery is confirmed"
                />
                <SecurityFeature
                  title="QR Code Verification"
                  description="Secure package delivery with unique QR codes"
                />
                <SecurityFeature title="Data Encryption" description="All personal data and messages are encrypted" />
                <SecurityFeature
                  title="Fraud Prevention"
                  description="Admin oversight and reporting system to prevent scams"
                />
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-green-700 text-white">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to Connect Your Village?</h2>
          <p className="text-xl mb-8 max-w-2xl mx-auto">
            Join thousands of users already buying, selling, and delivering across remote communities.
          </p>
          <Button size="lg" className="bg-white text-green-800 hover:bg-gray-100">
            Download the App
          </Button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <h3 className="text-xl font-bold mb-4">Village Connect</h3>
              <p className="text-gray-400">Connecting remote communities to the global marketplace.</p>
            </div>
            <div>
              <h3 className="text-xl font-bold mb-4">Quick Links</h3>
              <ul className="space-y-2">
                <li>
                  <Link href="#" className="text-gray-400 hover:text-white">
                    About Us
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-gray-400 hover:text-white">
                    How It Works
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-gray-400 hover:text-white">
                    For Businesses
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-gray-400 hover:text-white">
                    Support
                  </Link>
                </li>
              </ul>
            </div>
            <div>
              <h3 className="text-xl font-bold mb-4">Contact</h3>
              <address className="text-gray-400 not-italic">
                <p>Email: info@villageconnect.com</p>
                <p>Phone: +234 800 123 4567</p>
              </address>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-500">
            <p>&copy; {new Date().getFullYear()} Village Connect. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

function FeatureCard({ icon, title, description }) {
  return (
    <Card>
      <CardHeader>
        <div className="bg-green-100 w-12 h-12 rounded-full flex items-center justify-center text-green-700 mb-4">
          {icon}
        </div>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <CardDescription className="text-base">{description}</CardDescription>
      </CardContent>
    </Card>
  )
}

function SecurityFeature({ title, description }) {
  return (
    <li className="flex items-start">
      <div className="mr-3 mt-1">
        <Shield className="h-5 w-5 text-green-600" />
      </div>
      <div>
        <h4 className="font-semibold">{title}</h4>
        <p className="text-gray-600">{description}</p>
      </div>
    </li>
  )
}
