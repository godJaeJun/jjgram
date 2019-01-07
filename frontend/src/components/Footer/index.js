import React from 'react';
import './index.css';
//context는 해당 텍스트를 번역할 때 사용하는 것
const Footer = (props, context) => (
    <footer className="Footer">
      <div className="Column">
        <nav className="Nav">
          <ul className="List">
            <li className="List-item">About Us</li>
            <li className="List-item">Support</li>
            <li className="List-item">Blog</li>
            <li className="List-item">Press</li>
            <li className="List-item">API</li>
            <li className="List-item">Jobs</li>
            <li className="List-item">Privacy</li>
            <li className="List-item">Terms</li>
            <li className="List-item">Directory</li>
            <li className="List-item">Language</li>
          </ul>
        </nav>
      </div>
      <div>
        <span className="Copyright">© 2018 JJgram</span>
      </div>
    </footer>
);
export default Footer;